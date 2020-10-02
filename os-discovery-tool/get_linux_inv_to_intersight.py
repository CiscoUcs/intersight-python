#!/usr/bin/python3
"""
OS Discovery Tool (ODT) is a scripted/automated way to get the OS Inventory of Servers running in your
on-premise network to Intersight. It uses ssh access via 'authorized_keys' to extract the data from the Server OS.
Once the OS Inventory is extracted, it verifies if there are differences between what was extracted and what Intersight
sees. If there are differences, it used Intersight python SDK to upload the OS Inventory to intersight.
"""
import os
import sys
import subprocess
import json
import datetime
import argparse
from enum import Enum


class Bcolors:
    """This class is used for background color decorations of console output lines."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


try:
    import intersight
    from intersight.intersight_api_client import IntersightApiClient
    from intersight.apis import compute_blade_api as computeBlade
    from intersight.apis import compute_rack_unit_api as computeRackUnit
    from intersight.rest import ApiException
except ImportError as import_error:
    print((Bcolors.FAIL +
           "[ERROR]: Import for Intersight SDK modules failed. " +
           Bcolors.ENDC))
    print((Bcolors.BOLD + "[ERROR-DETAIL]: " +
           import_error.__str__() + Bcolors.ENDC))
    print((Bcolors.BOLD +
           "[ERROR-DETAIL]: Try re-installing it: "
           "'pip install git+https://github.com/CiscoUcs/intersight-python.git'" +
           Bcolors.ENDC))
    exit()


class ExecType(Enum):
    """This class identifies whether this is command, script or sudo command to be remotely executed."""
    COMMAND = 'command'
    SCRIPT = 'script'
    SUDO = 'sudo'


class QueryType(Enum):
    """This class identifies whether this is an os version or driver version query."""
    OS = 'os'
    DRIVER = 'driver'


class OsType:
    """This class broadly identifies OS categories."""
    SUSE = ["Suse", "Sles"]
    DEBIAN = ["Ubuntu"]
    REDHAT = ["Red Hat", "Rhel", "Centos"]
    ORACLE = ["Ol"]


class ValidationResult(Enum):
    """Support for validation result codes."""
    FAILURE = 'VALIDATION_FAILED'
    SUCCESS = 'VALIDATION_SUCCESS'


class FileHandlingException(RuntimeError):
    """Custom Exception to catch any exception while handling file operations."""

    def __init__(self, arg):
        self.message = arg


class HostManager:
    """Blueprint of interaction with the Host OS of Servers listed in the hosts file."""

    def __init__(self, hosts_file):
        self.hosts_file = hosts_file.strip()
        self.hosts = []
        self.num_hosts = 0

    def get_hosts(self):
        """Extract a list of hosts from the specified hosts file."""
        try:
            hosts_file = open(self.hosts_file, "r", encoding="utf-8")
            for host in hosts_file.readlines():
                if host.strip():
                    self.hosts.append(host.strip())
            self.num_hosts = len(self.hosts)
        except BaseException:
            raise FileHandlingException(
                Bcolors.FAIL +
                "[ERROR]: Unable to open the hosts file. Please ensure that correct hosts file path is specified in the Config file." +
                Bcolors.ENDC)

    @staticmethod
    def host_tools_validated(host, os_type):
        """Validates that the necessary tools are installed on the target servers."""
        if os_type == OsType.SUSE:
            cmd = "ssh " + host.strip() + " \'bash -s\' < suse-validate-tools.sh"
        else:
            cmd = "ssh " + host.strip() + " \'bash -s\' < validate-tools.sh"
        validation_result = str(
            (subprocess.check_output(['bash', '-c', cmd])), 'utf-8').strip()
        if validation_result == ValidationResult.FAILURE:
            return False
        return True

    def process_hosts(self, intersight_connection, env_config):
        """Core functions to process hosts i.e., collect inventory, diff and push changes to Intersight."""
        for host in self.hosts:
            print("--------------------------------------------------------------")
            print((Bcolors.BOLD +
                   "[INFO]: Processing host: " +
                   host.strip() +
                   Bcolors.ENDC))
            print("--------------------------------------------------------------")
            try:
                server_moid = intersight_connection.lookup_server_by_serial(
                    host)
                os_inv_reader = OsInvReader(host)
                os_inv_reader.get_os_inv()
                if server_moid and HostManager.host_tools_validated(
                        host, os_inv_reader.os_type):
                    driver_inv_reader = DriverInvReader(
                        host, os_inv_reader.os_type, intersight_connection.host_type)
                    driver_inv_reader.get_driver_inv()
                    os_inv_collection = os_inv_reader.os_inv_collection + \
                        driver_inv_reader.os_inv_collection

                    if env_config.logging:
                        env_config.write_log(
                            "[" + host.strip() + "]: Intersight MO Identifier: " + str(server_moid))
                        env_config.write_log(
                            "[" + host.strip() + "]: Building OS Inventory Collection... ")
                        env_config.write_log(json.dumps(os_inv_collection,
                                                        indent=4,
                                                        sort_keys=True,
                                                        separators=(',', ': '),
                                                        ensure_ascii=True))
                        env_config.write_log(
                            "--------------------------------------------------------------")
                    else:
                        print(
                            ("[" + host.strip() + "]: Intersight MO Identifier: " + str(server_moid)))
                        print(
                            ("[" + host.strip() + "]: Building OS Inventory Collection... "))
                        print((json.dumps(os_inv_collection,
                                          indent=4,
                                          sort_keys=True,
                                          separators=(',', ': '),
                                          ensure_ascii=True)))
                        print(
                            "--------------------------------------------------------------")

                    if intersight_connection.server_tags_differ(
                            os_inv_collection):
                        print(
                            (
                                Bcolors.OKBLUE +
                                "[" +
                                host.strip() +
                                "]: Changes detected in OS Inventory, pushing to intersight..." +
                                Bcolors.ENDC))
                        intersight_connection.patch_server_by_moid(
                            host, server_moid, os_inv_collection)
                    else:
                        print((Bcolors.WARNING +
                               "[" +
                               host.strip() +
                               "]: No Changes detected in OS Inventory, skipping..." +
                               Bcolors.ENDC))
                elif not server_moid:
                    print((Bcolors.FAIL +
                           "[" +
                           host.strip() +
                           "]: Server '" +
                           host.strip() +
                           "' look up by SERIAL number did not return any results." +
                           Bcolors.ENDC))
                    print((Bcolors.BOLD +
                           "[ERROR-DETAIL]: Please verify that '" +
                           host.strip() +
                           "' is connected and claimed in Intersight." +
                           Bcolors.ENDC))
                else:
                    print((Bcolors.FAIL +
                           "[ERROR]: Tools validation for host failed: " +
                           host.strip() +
                           Bcolors.ENDC))
                    print(
                        (
                            Bcolors.BOLD +
                            "[ERROR-DETAIL]: Please ensure that '" +
                            host.strip() +
                            "' has 'lshw'(RHEL/Ubuntu/Centos)/'hwinfo'(SLES), 'pci-utils(lspci)' "
                            "and 'modinfo' installed and available." +
                            Bcolors.ENDC))
                    continue

            except ApiException as api_error:
                print((Bcolors.FAIL +
                       "[ERROR]: Communication with Intersight failed with return code." +
                       Bcolors.ENDC))
                print((Bcolors.BOLD +
                       "[ERROR-DETAIL]: Communication with Intersight failed with response: " +
                       api_error.__str__() +
                       Bcolors.ENDC))
                print(
                    (
                        Bcolors.FAIL +
                        "[ERROR]: Could not complete ODT update (Intersight API returned errors) for server: " +
                        host.strip() +
                        Bcolors.ENDC))
                continue

            except subprocess.CalledProcessError as subprocess_error:
                print((Bcolors.BOLD +
                       "[ERROR-DETAIL]: SSH Communication with server failed with response: " +
                       subprocess_error.__str__() +
                       Bcolors.ENDC))
                print(
                    (
                        Bcolors.FAIL +
                        "[ERROR]: Could not complete ODT update (ssh communication failed) for server: " +
                        host.strip() +
                        Bcolors.ENDC))
                continue

            except KeyboardInterrupt:
                print((Bcolors.BOLD +
                       "[ERROR-DETAIL]: User initiated ABORT! " +
                       Bcolors.ENDC))
                print((Bcolors.FAIL +
                       "[ERROR]: Something didn't add up! Give the ODT another try?" +
                       Bcolors.ENDC))
                exit()


class InvReader:
    """Base class for reading the Inventory."""

    def __init__(self):
        self.host = ""
        self.os_type = ""
        self.os_inv_collection = []

    @property
    def tag_prefix(self):
        """Tag prefix for internal tags that are used for HCL validation."""
        return "intersight.server.os."

    @property
    def iso_8601_time(self):
        """Compute Time stamp to use for the updateTimestamp tag."""
        date_str = str(datetime.datetime.utcnow().isoformat())
        date_str = date_str[:-3] + "Z"  # type: str
        return date_str

    def invoke_shell(self, exec_type, query_type, name):
        """Invoke remote shell command."""
        output = None
        if exec_type == ExecType.SCRIPT:
            cmd = "ssh " + self.host.strip() + " \'bash -s\' < " + name
        elif exec_type == ExecType.COMMAND:
            cmd = "ssh " + self.host.strip() + " " + name
        elif exec_type == ExecType.SUDO:
            cmd = "ssh -t 2>/dev/null " + self.host.strip() + " \'bash -s\' " + name
        if query_type == QueryType.OS:
            output = str(subprocess.check_output(
                ['bash', '-c', cmd]), 'utf-8').strip()
        elif query_type == QueryType.DRIVER:
            output = str(subprocess.check_output(
                ['bash', '-c', cmd]), 'utf-8').split("\n")
        return output

    def add_item(self, item_type, key, value):
        """Add tag item."""
        full_key = self.tag_prefix + key
        if item_type == QueryType.OS:
            os_inv = dict()
            os_inv["Key"] = full_key
            os_inv["Value"] = value
            self.os_inv_collection.append(os_inv.copy())
        elif item_type == QueryType.DRIVER:
            driver_inv = dict()
            driver_inv["Key"] = full_key
            driver_inv["Value"] = value
            self.os_inv_collection.append(driver_inv.copy())


class OsInvReader(InvReader):
    """Collect OS specific data (other than that device and driver data)."""

    def __init__(self, host_name):
        InvReader.__init__(self)
        self.host = host_name

    def get_os_inv(self):
        """Collect OS specific data (other than that device and driver data)."""
        print(("[" + self.host.strip() + "]: Extracting OS Inventory... "))
        kernel_version = self.invoke_shell(
            ExecType.COMMAND,
            QueryType.OS,
            " uname -r | awk '{print $1}'")
        os_type = self.invoke_shell(
            ExecType.COMMAND,
            QueryType.OS,
            " uname -s | awk '{print $1}'")
        os_arch = self.invoke_shell(
            ExecType.COMMAND,
            QueryType.OS,
            " uname -m | awk '{print $1}'")
        os_vendor = (
            self.invoke_shell(
                ExecType.SCRIPT,
                QueryType.OS,
                "osvendor.sh")).lower().title()
        os_flavor = os_vendor

        if os_vendor in OsType.DEBIAN:
            self.os_type = OsType.DEBIAN
            os_flavor = (
                self.invoke_shell(
                    ExecType.SCRIPT,
                    QueryType.OS,
                    "debian-os-version.sh")).rstrip(",")
        elif os_vendor in OsType.SUSE:
            self.os_type = OsType.SUSE
            os_flavor = (
                self.invoke_shell(
                    ExecType.SCRIPT,
                    QueryType.OS,
                    "suse-os-version.sh"))
        elif os_vendor in OsType.ORACLE:
            self.os_type = OsType.ORACLE
            os_flavor = (
                self.invoke_shell(
                    ExecType.SCRIPT,
                    QueryType.OS,
                    "oracle-os-version.sh"))
        elif not os_vendor:
            os_vendor = (
                self.invoke_shell(
                    ExecType.SCRIPT,
                    QueryType.OS,
                    "osvendor-legacy.sh")).lower().title()
            self.os_type = OsType.REDHAT
        else:
            self.os_type = OsType.REDHAT

        if os_vendor in OsType.REDHAT:
            if os_vendor == "Centos":
                os_name = self.invoke_shell(
                    ExecType.SCRIPT, QueryType.OS, "centos-os-name.sh")
            else:
                os_name = self.invoke_shell(
                    ExecType.SCRIPT, QueryType.OS, "redhat-os-name.sh")
        elif self.os_type == OsType.DEBIAN:
            os_name = self.invoke_shell(
                ExecType.SCRIPT, QueryType.OS, "debian-os-name.sh")
        elif self.os_type == OsType.ORACLE:
            os_name = self.invoke_shell(
                ExecType.SCRIPT, QueryType.OS, "oracle-os-name.sh")
        else:
            os_name = "SuSE"

        if not os_name and os_vendor in OsType.REDHAT:
            os_name = self.invoke_shell(
                ExecType.SCRIPT,
                QueryType.OS,
                "centos-os-name-legacy.sh")

        if os_vendor == "Rhel":
            os_vendor = "Red Hat"
        elif os_vendor == "Centos":
            os_vendor = "CentOS"
        elif os_vendor == "Sles":
            os_vendor = "SuSE"
        elif os_vendor == "Ol":
            os_vendor = "Oracle Linux"

        self.add_item(QueryType.OS, "updateTimestamp", self.iso_8601_time)
        self.add_item(
            QueryType.OS,
            "kernelVersionString",
            os_name if os_vendor.lower().title() in OsType.REDHAT else os_flavor)
        self.add_item(QueryType.OS, "releaseVersionString", kernel_version)
        self.add_item(QueryType.OS, "type", os_type)
        self.add_item(QueryType.OS, "vendor", os_vendor)
        self.add_item(QueryType.OS, "name", os_name)
        self.add_item(QueryType.OS, "arch", os_arch)


class DriverInvReader(InvReader):
    """Collect device and driver data."""

    def __init__(self, hostname, os_type, host_type):
        InvReader.__init__(self)
        self.host = hostname
        self.os_type = os_type
        self.host_type = host_type

    def get_driver_inv(self):
        """Collect device and driver data."""
        print(("[" + self.host.strip() + "]: Extracting driver Inventory... "))
        if self.os_type == OsType.SUSE:
            drivers = self.invoke_shell(
                ExecType.SCRIPT,
                QueryType.DRIVER,
                "suse-netdriver.sh")
            versions = self.invoke_shell(
                ExecType.SCRIPT,
                QueryType.DRIVER,
                "suse-netversions.sh")
            descriptions = self.invoke_shell(
                ExecType.SCRIPT, QueryType.DRIVER, "suse-netdev.sh")

            drivers += self.invoke_shell(ExecType.SCRIPT,
                                         QueryType.DRIVER, "suse-storagedriver.sh")
            versions += self.invoke_shell(ExecType.SCRIPT,
                                          QueryType.DRIVER, "suse-storageversions.sh")
            descriptions += self.invoke_shell(ExecType.SCRIPT,
                                              QueryType.DRIVER, "suse-storagedev.sh")
        else:
            drivers = self.invoke_shell(
                ExecType.SCRIPT, QueryType.DRIVER, "netdriver.sh")
            versions = self.invoke_shell(
                ExecType.SCRIPT, QueryType.DRIVER, "netversions.sh")
            descriptions = self.invoke_shell(
                ExecType.SCRIPT, QueryType.DRIVER, "netdev.sh")
            fc_dev = self.invoke_shell(
                ExecType.SCRIPT, QueryType.DRIVER, "fcdev.sh")

            if fc_dev:
                descriptions += fc_dev
                drivers += self.invoke_shell(ExecType.SCRIPT,
                                             QueryType.DRIVER, "fcdriver.sh")
                versions += self.invoke_shell(ExecType.SCRIPT,
                                              QueryType.DRIVER, "fcversions.sh")

            drivers += self.invoke_shell(ExecType.SCRIPT,
                                         QueryType.DRIVER, "storagedriver.sh")
            versions += self.invoke_shell(ExecType.SCRIPT,
                                          QueryType.DRIVER, "storageversions.sh")
            descriptions += self.invoke_shell(ExecType.SCRIPT,
                                              QueryType.DRIVER, "storagedev.sh")

            os_vendor = self.invoke_shell(ExecType.SCRIPT,
                                          QueryType.OS, 'osvendor.sh').lower().title()

            # Invoke GPU scripts for OSes: Ubuntu, CentOS, Redhat
            if os_vendor in OsType.DEBIAN or os_vendor in OsType.REDHAT:
                gpu_info = self.invoke_shell(ExecType.SCRIPT,
                                             QueryType.DRIVER, 'gpudriver.sh')
                gpu_desc = self.invoke_shell(ExecType.SCRIPT,
                                             QueryType.DRIVER, 'gpudev.sh')

                if gpu_info:
                    for value in gpu_info:
                        if len(value) > 0:
                            drivers.append(value.split(',')[0].strip())
                            versions.append(value.split(',')[1].strip())
                    for value in gpu_desc:
                        if len(value) > 0:
                            descriptions.append(value)

        added_drivers = set()
        driver_count = 0

        for i, value in enumerate(drivers):
            if not value:
                continue

            if drivers[i] not in added_drivers:
                added_drivers.add(value)
            else:
                continue

            self.add_item(
                QueryType.DRIVER,
                "driver." + str(driver_count) + ".name", value.replace('"', ''))
            self.add_item(
                QueryType.DRIVER,
                "driver." +
                str(driver_count) +
                ".version",
                versions[i].lstrip("0"))
            self.add_item(
                QueryType.DRIVER,
                "driver." +
                str(driver_count) +
                ".description",
                descriptions[i])
            driver_count += 1


class IntersightConnectionManager:
    """Connect to Intersight and check for the differences in OS Inventory"""

    def __init__(self, api_key, api_secret_path, intersight_url):
        self.api_key = api_key
        self.api_secret_path = api_secret_path
        self.intersight_url = intersight_url
        self.server_tags = None
        self.user_tags = None
        self.host_type = None
        self.serial_number = None
        self.api_instance = None
        self.server_api = None
        self.results = None

    def connect(self):
        """Connect to Intersight."""
        self.api_instance = IntersightApiClient(
            host=self.intersight_url,
            private_key=self.api_secret_path,
            api_key_id=self.api_key)

    def disconnect(self):
        """Disconnect from intersight."""
        pass

    def lookup_server_by_serial(self, hostname):
        """Lookup if server is claimed in intersight."""
        print(("[" + hostname.strip() + "]: Extracting Server Serial Number... "))
        cmd = "ssh -t 2>/dev/null " + \
            hostname.strip() + " sudo /usr/sbin/dmidecode -s system-serial-number"
        host_serial = str((subprocess.check_output(
            ['bash', '-c', cmd])), 'utf-8').split("\n")
        if len(host_serial) > 1:
            for serial in host_serial:
                if serial and "#" not in serial:
                    self.serial_number = serial.strip()
        else:
            self.serial_number = host_serial.strip()

        print(("[" +
               hostname.strip() +
               "]: Host Serial Number: " +
               self.serial_number))
        cmd = "ssh -t 2>/dev/null " + \
            hostname.strip() + " sudo /usr/sbin/dmidecode -s system-product-name"
        host_type = str((subprocess.check_output(
            ['bash', '-c', cmd])), 'utf-8').split("\n")
        if len(host_type) > 1:
            for htype in host_type:
                if htype and "#" not in htype:
                    self.host_type = htype.strip()
        else:
            self.host_type = host_type[0].strip()

        print(("[" + hostname.strip() + "]: Host Model: " + self.host_type))
        if host_serial != "<BAD INDEX>":
            print(("[" + hostname.strip() +
                   "]: Extracting Server MO Identity from Intersight... "))
            if 'UCSB' in self.host_type:
                self.server_api = computeBlade.ComputeBladeApi(
                    self.api_instance)
                self.results = self.server_api.compute_blades_get(
                    inlinecount='allpages', top=100, filter='Serial eq ' + self.serial_number)
            elif 'UCSC' in self.host_type or 'HX' in self.host_type:
                self.server_api = computeRackUnit.ComputeRackUnitApi(
                    self.api_instance)
                self.results = self.server_api.compute_rack_units_get(
                    inlinecount='allpages', top=100, filter='Serial eq ' + self.serial_number)

            if self.results:
                print(("[" +
                       hostname.strip() +
                       "]: Server MO Identity: " +
                       self.results.results[0].moid))
                self.server_tags = [elem for elem in self.results.results[0].tags
                                    if 'intersight.server.os.' in elem.to_dict()['key']]
                self.user_tags = [elem for elem in self.results.results[0].tags
                                  if 'intersight.server.os.' not in elem.to_dict()['key']]
                return self.results.results[0].moid
            return 0
        else:
            print(("[" +
                   hostname.strip() +
                   "]: Server SERIAL number invalid: " +
                   self.serial_number))
            return 0

    def patch_server_by_moid(self, hostname, moid, os_inv_collection):
        """Push Os Inventory changes to Intersight."""
        compute = intersight.ComputeBlade()
        compute.tags = os_inv_collection + self.user_tags
        print(("[" + hostname.strip() + "]: Patching Server MO with OS Inventory... "))
        if 'UCSB' in self.host_type:
            result = self.server_api.compute_blades_moid_patch(moid, compute)
        elif 'UCSC' in self.host_type or 'HX' in self.host_type:
            result = self.server_api.compute_rack_units_moid_patch(
                moid, compute)
        else:
            result = None

        if result is None:
            print("--------------------------------------------------------------")
            print((Bcolors.OKGREEN +
                   "[" +
                   hostname.strip() +
                   "]: OS Inventory push to Intersight completed!" +
                   Bcolors.ENDC))
            print("--------------------------------------------------------------")
        else:
            print("--------------------------------------------------------------")
            print((Bcolors.FAIL +
                   "[" +
                   hostname.strip() +
                   "]: {" +
                   result +
                   "}, OS Inventory push to Intersight failed!" +
                   Bcolors.ENDC))
            print("--------------------------------------------------------------")

    def server_tags_differ(self, os_inv_collection):
        """Check if OS Inventory collected and OS Inventory seen by Intersight differ."""
        changed = False
        if len(self.server_tags) != len(os_inv_collection):
            changed = True
        else:
            for new_elem in os_inv_collection:
                if new_elem['Key'] != 'intersight.server.os.updateTimestamp':
                    old_elem = [elem for elem in self.server_tags if elem.to_dict()[
                        'key'] == new_elem['Key']][0]
                    if old_elem is None or old_elem.to_dict(
                    )['value'] != new_elem['Value']:
                        changed = True
                        break
        return changed


class EnvironmentConfigurator:
    """Class for Managing Environment context."""

    def __init__(self, logging, configs):
        self.hosts_file = configs['config']['hosts_file_path']
        self.logfile_path = configs['config']['logfile_path'] + "/" + \
            'intersight_os_discovery_' + datetime.datetime.utcnow().isoformat() + '.log'
        self.api_key = configs['config']['intersight_api_key']
        self.secret_key_path = configs['config']['intersight_secret_file']
        self.intersight_url = configs['config']['intersight_url']
        self.logging = logging
        self.log_file = None
        self.options = None

    def init_log_file(self):
        """Open log file in specified location."""
        try:
            if self.logging is not None and self.logging is True:
                print((Bcolors.WARNING +
                       '[INFO]: Using logging mode...' +
                       Bcolors.ENDC))
                print((Bcolors.WARNING +
                       '[INFO]: Using log file: ' +
                       self.logfile_path +
                       Bcolors.ENDC))
                self.log_file = open(self.logfile_path, 'w', encoding='utf-8')
            else:
                print((Bcolors.WARNING +
                       '[INFO]: Logging disabled...' +
                       Bcolors.ENDC))
        except BaseException:
            raise FileHandlingException(
                Bcolors.FAIL +
                "[ERROR]: Unable to find the log file path. Please ensure that correct log file path is specified in the Config file." +
                Bcolors.ENDC)

    def close_log_file(self):
        """Close already opened log file."""
        self.log_file.close()

    def write_log(self, log_line):
        """Write log file entries prefixed by timestamp."""
        timestamped_log_line = "[" + \
            str(datetime.datetime.utcnow()) + "]" + log_line + '\n'
        self.log_file.write(str(timestamped_log_line.encode('utf8')))

    @staticmethod
    def set_exec_path():
        """Set Execution path."""
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)

    @staticmethod
    def check_python_ver():
        """Check Python version (this utility only supports Python 3)"""
        if sys.version_info[0] < 3:
            print(
                (
                    Bcolors.FAIL +
                    "[ERROR]: Ensure that you have Python 3 (3.7 or later) installed to run this utility. " +
                    Bcolors.ENDC))
            print((Bcolors.BOLD +
                   "[ERROR-DETAIL]: Usage of Python 3 is highly recommended." +
                   Bcolors.ENDC))
            print(
                (
                    Bcolors.BOLD +
                    "[ERROR-DETAIL]: To use Python 2, use 'get_linux_inv_to_intersight.py2' file." +
                    Bcolors.ENDC))
            exit()

    @staticmethod
    def process_command_args():
        """Process arguments and setup environment context."""
        parser = argparse.ArgumentParser(
            description='ODT: Utility to import OS Inventory of your Linux Environment to Intersight.')
        parser.add_argument(
            "-l",
            "--log-inventory",
            action="store_true",
            dest="logging",
            help="[OPTIONAL] Log OS Inventory to log file location configured")
        parser.add_argument(
            "-f",
            "--configfile",
            dest="configfile",
            help="[MANDATORY] Filesystem path to configuration file for ODT")
        args = parser.parse_args()
        if args.configfile is None:
            print(args)
            print((Bcolors.FAIL +
                   "[ERROR]: Please provide MANDATORY arguments" +
                   Bcolors.ENDC))
            print((Bcolors.WARNING +
                   "[HINT]: try $ ./get_linux_inv_to_intersight.py --help" +
                   Bcolors.ENDC))
            exit()

        return args

    @staticmethod
    def read_configs(configfile):
        """Read configuration from specified config file."""
        json_data = None
        configs = None
        try:
            json_data = open(configfile.strip()).read()
        except BaseException:
            raise FileHandlingException(
                Bcolors.FAIL +
                "[ERROR]: Unable to find the config file path. Please ensure that correct config file path is specified." +
                Bcolors.ENDC)
        try:
            configs = json.loads(json_data)
        except BaseException:
            raise FileHandlingException(
                Bcolors.FAIL +
                "[ERROR]: Unable to process the config file. Please ensure that config file is in proper JSON format." +
                Bcolors.ENDC)

        return configs


def do_discovery():
    """Main Execution flow for ODT."""
    print((Bcolors.OKGREEN +
           "[ODT: START-TIMESTAMP: " +
           str(datetime.datetime.utcnow()) +
           "]" +
           Bcolors.ENDC))

    EnvironmentConfigurator.check_python_ver()
    options = EnvironmentConfigurator.process_command_args()
    configs = EnvironmentConfigurator.read_configs(options.configfile.strip())

    EnvironmentConfigurator.set_exec_path()

    env_config = EnvironmentConfigurator(options.logging, configs)

    if env_config.logging:
        env_config.init_log_file()
        env_config.write_log(
            "------------------------START-TIMESTAMP--------------------------")
    else:
        print((Bcolors.WARNING + '[INFO]: Logging disabled...' + Bcolors.ENDC))

    host_manager = HostManager(env_config.hosts_file)
    host_manager.get_hosts()

    print(("[INFO]: Found " +
           str(host_manager.num_hosts) +
           " hosts in " +
           env_config.hosts_file))

    intersight_connection = IntersightConnectionManager(
        env_config.api_key.strip(),
        env_config.secret_key_path.strip(),
        env_config.intersight_url.strip())

    intersight_connection.connect()

    host_manager.process_hosts(intersight_connection, env_config)

    print("--------------------------------------------------------------")
    print((Bcolors.BOLD +
           "[INFO]: ODT push to Intersight completed!" +
           Bcolors.ENDC))
    print("--------------------------------------------------------------")

    if env_config.logging:
        env_config.write_log(
            "-----------------------END-TIMESTAMP--------------------------")
        env_config.close_log_file()

    print((Bcolors.OKGREEN +
           "[ODT: END-TIMESTAMP: " +
           str(datetime.datetime.utcnow()) +
           "]" +
           Bcolors.ENDC))


if __name__ == '__main__':
    try:
        do_discovery()
    except FileHandlingException as e:
        print((e.message))
        exit()
    except Exception as err:
        print((Bcolors.FAIL +
               "[ERROR]: An error has occured while processing the given information: " +
               Bcolors.ENDC))
        print((Bcolors.BOLD + "[ERROR-DETAIL]: " + str(err) + Bcolors.ENDC))
        exit()