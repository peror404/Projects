
Banner-Grabber: Advanced Port Scanning and Banner Grabbing with Nikto
Banner-Grabber is a Bash script designed to perform advanced port scanning and banner grabbing. It allows you to scan specific ports or a range of ports on a target IP address and optionally perform a Nikto web server scan. The results can be saved to an output file, making it useful for penetration testing, network auditing, and vulnerability assessments.

This script also integrates with a Python script (banner_grabber.py) that handles the actual banner grabbing and port scanning operations.

Features
Port Scanning: Scan specific ports or a range of ports on the target machine.
Banner Grabbing: Grabs banners from open ports to gather information about the services running.
Nikto Scan: Run a Nikto web server scan to detect vulnerabilities.
Output File: Save the results of the scan to a file for further analysis.
Command-Line Interface: User-friendly CLI for specifying the target and scan options.
Prerequisites
Before running the script, ensure that the following dependencies are installed:

Python 3: The script uses Python for banner grabbing.
Nikto: A web scanner to test for common vulnerabilities on HTTP servers.
You can install the required dependencies as follows:

For Python 3:

bash
Copy code
sudo apt-get install python3
For Nikto:
sudo apt-get install nikto
Installation
Clone this repository or download the files to your local machine.

Make the banner_grabber.sh script executable:
chmod +x banner_grabber.sh
Ensure the banner_grabber.py Python script is available and in the same directory or set the correct path in the Bash script.

Usage
You can run the script with several options for different types of scans. The syntax is as follows:
./banner_grabber.sh [-t target_ip] [-s specific_ports] [-r start_port-end_port] [-o output_file] [-h]
Options:
-t <target_ip>
Required: The IP address of the target system to scan.

-s <specific_ports>
Optional: A comma-separated list of specific ports to scan (e.g., 80,443,22). If specified, only these ports will be scanned.

-r <start_port-end_port>
Optional: A port range to scan (e.g., 1-1024). If specified, only the range of ports will be scanned.

-o <output_file>
Optional: Specify an output file where the results of the Nikto scan will be saved.

-h
Optional: Show the help message and usage instructions.

Examples:
Scan specific ports (22, 80, 443) on target IP 192.168.1.1 and save the results to a file:

./banner_grabber.sh -t 192.168.1.1 -s 22,80,443 -o nikto_results.txt
Scan a range of ports (1-1024) on target IP 192.168.1.1:

./banner_grabber.sh -t 192.168.1.1 -r 1-1024
Scan the default port range (1-1024) on target IP 192.168.1.1:
./banner_grabber.sh -t 192.168.1.1
Scan specific ports and run a Nikto scan (saving results to a file):
./banner_grabber.sh -t 192.168.1.1 -s 80,443 -o nikto_results.txt
                                   
How It Works
Print Banner:
                                   
The script starts by displaying a banner with the name of the tool to indicate that the scan is about to begin.

Dependency Check:
The script checks whether Python 3 and Nikto are installed. If either is missing, the script exits and prompts you to install the necessary software.

Command-Line Parsing:
The script parses the provided options to determine the target IP address, specific ports or port range, and any output file for saving Nikto results.

Run the Banner Grabber Python Script:
The script then invokes the banner_grabber.py Python script, passing the relevant options (target, ports, output file).

Nikto Scan:
The script runs a Nikto scan after the banner grabbing is done. The results are saved to the specified output file, if provided.
