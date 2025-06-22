# Nmap Scan Reporter 🔍

A simple Python cybersecurity tool that runs Nmap scans, parses the results, and highlights open ports, services, and potential vulnerabilities.

## Features

- Run Nmap with version + OS detection
- Parse output for open ports and service versions
- Detect vulnerable services using simple version checks
- Clean console-based summary

## Requirements

- Python 3.x
- Nmap installed (`sudo apt install nmap`)

## Usage

```bash
python3 scan.py
```
Then enter a target IP (e.g. scanme.nmap.org or your local IP).

