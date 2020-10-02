#!/bin/bash
export PATH=$PATH:/sbin:/usr/sbin
lshwcmd=`which lshw`
lspcicmd=`which lspci`
modinfocmd=`which modinfo`
osvendor=$(cat /etc/*-release 2>/dev/null | grep -i ^ID= | head -n1 | awk -F"=" '{print $2}'| xargs)
nvidiasmicmd=`which nvidia-smi 2>&1`
invalid=" |'"

# List of OS vendors who support nvidia drivers
declare -a osvendorlist=("ubuntu" "centos" "rhel" "red hat")

for pciaddress in $(${lshwcmd} -C Display 2>/dev/null | grep "pci@" | awk -F":" '{print $3":"$4}');
  do
     # Identify the classcode is "3D Controller" or "VGA controller" for the Nvidia GPU
     classcode=$(${lspcicmd} -v -s ${pciaddress} | grep -i "VGA compatible controller\|3d controller" | awk -F":" '{print $2}' | awk -F" " '{print $2" "$3" "$4}' | xargs)
     driver=$(${lspcicmd} -v -s ${pciaddress} | grep "Kernel driver" | awk -F":" '{print $2}' | xargs);

     # Check if the nvidia-smi drivers are installed correctly
     if ! ([[ $nvidiasmicmd =~ $invalid || -z "$nvidiasmicmd" ]]);
     then

       nvidiagpuname=$(nvidia-smi --query-gpu=name --format=csv,noheader)
       nvidiagpuversion=$(${lspcicmd} -v -s $pciaddress | grep "Kernel driver" | awk -F":" '{print $2}' | xargs ${modinfocmd} 2>/dev/null | grep -i "version" | head -n1 | awk '{print $2}' | xargs)
       nvidiavgpu=$(nvidia-smi vgpu)

       # support for nvidia drivers only
       if [[ ($driver == "nvidia")]];
          then
          if [[ ($nvidiagpuname == "Tesla M6") || ($nvidiagpuname == "Tesla M60") ]];
              then
              # Ubuntu, CentOS support only compute drivers
              # Redhat OS supports both graphics and compute drivers
              if [[ (${osvendorlist[*]} =~ ${osvendor}) ]] && [[ ($classcode == "3D controller")]];
                  then
                  echo "${driver}(compute), ${nvidiagpuversion}"
              # If the mode is not set correctly on M6/M60 GPUs
              elif [[ (${osvendorlist[*]} =~ ${osvendor}) ]] && [[ ($classcode =~ "VGA")]];
                  then
                  echo "${driver}(compute), ''"
              fi

              # evaluating graphics drivers of on Redhat OS
              if [[ ($osvendor == "rhel") || ($osvendor == "red hat") ]] && [[ ($classcode =~ "VGA") ]];
                  then
                  echo "${driver}(graphics), ${nvidiagpuversion}"
              elif [[ ($osvendor == "rhel") || ($osvendor == "red hat") ]] && [[ ($classcode == "3D controller")]];
                  then
                  echo "${driver}(graphics), ''"
              fi

          else
            if [[ (${osvendorlist[*]} =~ ${osvendor}) ]] && [[ ($nvidiavgpu == "Not supported devices in vGPU mode")]];
                then
                echo "${driver}(compute), ${nvidiagpuversion}"
            elif [[ ($osvendor == "rhel") || ($osvendor == "red hat") ]] && [[ !($nvidiavgpu == "Not supported devices in vGPU mode") ]];
                then
                echo "${driver}(graphics), ${nvidiagpuversion}"
             fi
          fi
      fi

     # check if GPU is in passthru mode
     elif [[ ($osvendor == "rhel") || ($osvendor == "red hat") ]] && [[ ($driver == "vfio-pci") ]];
     then
        continue
     fi
done