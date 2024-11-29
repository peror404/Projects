import argparse
import socket
import re
import subprocess
import pyfiglet

# ASCII Banner using pyfiglet
def print_banner():
    banner = pyfiglet.figlet_format("BANNER-GRABBER", font="slant", width=400)
    print(banner)
    print("==========================================")
    print("    By_Abhinav_Ankit_Harsh_Harshit")
    print("==========================================")
# Function to scan open ports on a target IP address
def scan_ports(target_ip, port_list=None, start_port=1, end_port=1024):
    open_ports = []
    
    if port_list:
        print(f"Scanning specific ports: {port_list} on {target_ip}...\n")
        ports_to_scan = port_list
    else:
        print(f"Scanning {target_ip} for open ports from {start_port} to {end_port}...\n")
        ports_to_scan = range(start_port, end_port + 1)
    
    for port in ports_to_scan:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"Port {port} is open.")
        sock.close()
    
    return open_ports

# Function to grab the server information on a given port
def grab_server_info(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target_ip, port))
        sock.send(b"HEAD / HTTP/1.0\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
        response = sock.recv(1024).decode().strip()
        sock.close()
        return response
    except socket.error:
        return None

# Function to extract server and version information from a response using regex
def extract_server_info(response):
    server_info_regex = r"Server:\s*(.+)"
    version_regex = r"(\d+\.\d+\.\d+|\d+\.\d+)"
    
    server = re.search(server_info_regex, response)
    version = re.findall(version_regex, response)
    
    server_name = server.group(1) if server else "Server information not found"
    version_number = version[0] if version else "Version not found"
    
    return server_name, version_number

# Function to run Nikto command and save results to file
def run_nikto(target_ip, open_ports, output_file=None):
    print("\nRunning Nikto for more information...\n")
    for port in open_ports:
        command = f"nikto -h {target_ip}:{port} -C all"
        print(f"Executing: {command}")
        
        try:
            if output_file:
                with open(output_file, "a") as f:
                    f.write(f"\nNikto results for port {port}:\n")
                    subprocess.run(command, shell=True, check=True, stdout=f, stderr=f)
            else:
                subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Nikto on port {port}: {e}")

# Main function to handle input, scan ports, retrieve server info, and write open ports to file
def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description='Scan ports and grab server information.')
    parser.add_argument('-t', '--target', required=True, help='Target IP address')
    parser.add_argument('-s', '--specific', help='Specific ports (comma-separated)')
    parser.add_argument('-r', '--range', nargs=2, type=int, help='Port range (start end)')
    parser.add_argument('-o', '--output', help='Output file for Nikto results')
    
    args = parser.parse_args()

    target_ip = args.target
    specific_ports = args.specific
    port_range = args.range
    output_file = args.output

    open_ports = []

    if specific_ports:
        specific_ports_list = list(map(int, specific_ports.split(',')))
        open_ports = scan_ports(target_ip, port_list=specific_ports_list)
    elif port_range:
        start_port, end_port = port_range
        open_ports = scan_ports(target_ip, start_port=start_port, end_port=end_port)
    else:
        print("No specific ports or range provided. Scanning default range of ports (1 to 1024).")
        open_ports = scan_ports(target_ip)

    if open_ports:
        print("\nGrabbing server information from open ports...\n")
        with open("open_ports.txt", "w") as f:
            for port in open_ports:
                response = grab_server_info(target_ip, port)
                if response:
                    print(f"Port {port} - Server Response:\n{response}")
                    server, version = extract_server_info(response)
                    print(f"Server: {server}\nVersion: {version}\n")
                else:
                    print(f"Port {port} - No response received or service unknown.\n")
                f.write(f"{port}\n")
        
        print("\nOpen ports saved to open_ports.txt")
        
        if output_file:
            run_nikto(target_ip, open_ports, output_file=output_file)
        else:
            run_nikto(target_ip, open_ports)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()