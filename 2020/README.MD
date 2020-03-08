
<h1>WARNING: WILL NOT WORK IF THERE ARE NO CAMERAS CONNECTED</h1>
<p>
**<h1>Requirements</h1>**
To run the chameleon server, you must have JDK 12 or higher installed on your co-processor.**[Download JDK 12 here.](https://bell-sw.com/pages/liberica_install_guide-12.0.2/)**
<p>
**<h1>Running the server</h1>**
**Windows**
for windows, run in the command prompt:

	chameleon-vision-2.3.1-RELEASE.jar
<p>
**Linux / Mac**
for linux / mac, run in the terminal:
	
	$ sudo java -jar chameleon-vision-X.X.X-RELEASE.jar
<p>


**<h2>Command-Line Arguments</h2>**

Chameleon Vision supports a few command-line arguments to enable or disable certain features, or to change operation parameters.

Arguments:
1. <code>--nt-servermode</code>
	1. Description:
		Enables an internal NetworkTables Server, which acts as a networkTables 		simulator.
	2. Parameters:
		None.
2. <code>--nt-client-server</code>
	1. Description:
		Sets a manual IP address for the NT CLient to connect to.
	2. Parameters:
		IP address.
		(i.e. <code>10.8.32.2</code>
3. <code>--unmanage-network</code>
	1. Description:
		Disables the automatic network settings manager.
	2. Parameters:
		None
<p>

**<h1>Putting data on the NetworkTables server</h1>**
You can use the tecbotVision.py python script to put certain data on the tecbotVision table.
<p>

**<h2>NetworkTables Server testing</h2>**
Use <code>ifconfig</code> (mac / linux) and <code>ipconfig</code> to get the ip of this computer.
<p>
To test that the network tables server is running, use the "global_listener.py" python script and execute it. This script will detect global variable changes in all tables running in the NetworkTables server.
Repo directory: TecbotVision/2020/python_scripts/global_listener.py
command: py global_listener.py
<p>
Another test you can run is robot_example.py . This script will put an incrementing value periodically on the SmartDashboard table in the NetworkTables server.
Repo directory: TecbotVision/2020/python_scripts/robot_example.py
command: py robot_example.py

