# Nmap Scan Reporter 🔍

A simple Python cybersecurity tool that runs Nmap scans, parses the results, and highlights open ports, services, and potential vulnerabilities.

## Features

- Run Nmap with version + OS detection
- Parse output for open ports and service versions
- Detect vulnerable services using simple version checks
- Clean console-based summary

## How It Works 

1. ### User inputs target IP or hostname
When you run python3 scan.py, the script asks for a target to scan (e.g., scanme.nmap.org or your local IP).

2. ### Runs Nmap scan with version and OS detection
The script runs an Nmap command in the background to scan the target’s open ports, services, and operating system.

3. ### Saves raw Nmap output to a file
The output is saved in the output/ folder as a text file for later analysis.

3. ### Parses the scan results
The parser reads the saved Nmap file, extracts open ports, service versions, and attempts to identify potential vulnerabilities based on known version issues.

4. ### Displays a clean summary in the console
Finally, the script prints an easy-to-read summary of open ports, detected services, OS guess, and any vulnerability warnings.

## Requirements

- Python 3.x
- Nmap installed (`sudo apt install nmap`)

## Usage

```bash
python3 scan.py
```
Then enter a target IP (e.g. scanme.nmap.org or your local IP).

