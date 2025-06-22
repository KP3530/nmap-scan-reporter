# Python can run terminal commands using subprocess. It gives us more control than os.system
import subprocess
from parse_results import parse_nmap_output

def run_nmap_scan(target):
    print(f"[+] Scanning {target} ...")
    output_file = f"output/{target.replace('.', '_').replace('/', '_')}.txt"

    # Run Nmap with version detection and OS detection
    command = ['nmap', '-sV', '-O', '-oN', output_file, target]
    subprocess.run(command)

    print(f"[+] Scan complete. Output saved to {output_file}")

    # Parse and summarize results
    parse_nmap_output(output_file, target)

if __name__ == "__main__":
    target = input("Enter IP or subnet (e.g., 192.168.1.1 or scanme.nmap.org): ")
    run_nmap_scan(target)
