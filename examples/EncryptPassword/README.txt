This folder contains the executables that needs to be called from the command line to encrypt the password in the CIMC recognisable format. 
INPUT: 	username, password. 
OUTPUT: 	
		On success:
			encrypted password. 
		On Failure: 
			Below return codes:
			1 - Pycrypto is not installed
			2 - Wrong number of arguments provided to the executable
			3 - Username exceeds allowed max characters
			4 - Password exceeds allowed max characters

Below are the steps to execute and dependencies for different platforms. 

1.For Linux
	- Executables for Linux is present under 'Linux' folder
	- Execute it as follows:
		./EncryptPassword <username> <password>
	-Dependencies:
		- Python needs to be installed on the host machine
		- pycrypto library is required
			- Download pycrypto-2.6.1 from https://pypi.python.org/pypi/pycrypto
			- To Install it run the below steps from the downloaded folder:
				- tar -zxf pycrypto-2.6.1.tar.gz
				- cd pycrypto-2.6.1
				- For python version > 3: python setup.py -q install --user --prefix= 2> /dev/null
				- For python version < 3: python setup.py -q install --user 2> /dev/null

2.For Mac OS
	- Executables for Mac OS is present under 'Mac' folder
	- Execute it as follows:
		./EncryptPassword <username> <password>
	-Dependencies:
		- Python needs to be installed on the host machine
		- pycrypto library is required
			- Download pycrypto-2.6.1 from https://pypi.python.org/pypi/pycrypto
			- To Install it run the below steps from the downloaded folder:
				- tar -zxf pycrypto-2.6.1.tar.gz
				- cd pycrypto-2.6.1
				- For python version > 3: python setup.py -q install --user --prefix= 2> /dev/null
				- For python version < 3: python setup.py -q install --user 2> /dev/null

3.For Windows
	- Executables for Windows is present under 'Windows' folder
	- Execute it as follows based on python version. Get the python version using command "python --version"
		- for python 2.7  : EncryptPassword_v27 <username> <password>
		- for python 3.3 : EncryptPassword_v33 <username> <password>
		- for python 3.4 : EncryptPassword_v34 <username> <password>
	-Dependencies:
		- Python needs to be installed.
			- Supported versions are : 2.7, 3.3, 3.4
			- Download any one of the above version from https://www.python.org/downloads/windows/
			- Run the executable to install the python
			- While installing, make sure to select the 'add Python.exe to PATH' option. This will allow to run python from any location whithout using absolute/relative path
		- pycrypto library is required
			- This needs to be same version as the python installed in the above step i.e., 2.7, 3.3, 3.4
			- Download the correct version from http://www.voidspace.org.uk/python/pycrypto-2.6.1/
			- Run the executable to install the pycrypto library

