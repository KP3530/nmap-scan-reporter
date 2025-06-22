def parse_nmap_output(filename, target_ip):
    with open(filename, 'r') as file:
        lines = file.readlines()

    open_ports = []
    os_guess = "Unknown"
    vuln_warnings = []

    ports_section = False

    for line in lines:
        line = line.strip()

        # OS Detection
        if line.startswith("OS details:"):
            os_guess = line[len("OS details:"):].strip()

        # Start of ports section
        if line.startswith("PORT"):
            ports_section = True
            continue

        # End of ports section
        if ports_section and line == "":
            ports_section = False
            continue

        # Parse open ports
        if ports_section:
            if '/tcp' in line and 'open' in line:
                parts = line.split()
                port = parts[0]
                state = parts[1]
                service = parts[2]
                version = ' '.join(parts[3:]) if len(parts) > 3 else 'N/A'

                open_ports.append({
                    'port': port,
                    'state': state,
                    'service': service,
                    'version': version
                })

    # Simple vulnerability hints
    for entry in open_ports:
        version = entry['version'].lower()
        service = entry['service'].lower()

        if "apache 2.4.29" in version:
            vuln_warnings.append(f"{entry['port']} ({entry['service']}): Apache 2.4.29 has known CVEs like CVE-2019-0211")
        elif "openssh 7.6" in version:
            vuln_warnings.append(f"{entry['port']} ({entry['service']}): OpenSSH 7.6p1 is vulnerable (CVE-2018-15473)")
        elif "nginx 1.14.0" in version:
            vuln_warnings.append(f"{entry['port']} ({entry['service']}): Nginx 1.14.0 had vulnerabilities in 2019")

    # Display results
    print("\n=== 🔍 Nmap Scan Summary ===")
    print(f"Target: {target_ip}")
    print(f"OS Guess: {os_guess}\n")

    print("Open Ports:")
    for entry in open_ports:
        print(f"- {entry['port']}: {entry['service']} ({entry['version']})")

    print("\nPotential Vulnerabilities:")
    if vuln_warnings:
        for warning in vuln_warnings:
            print(f"- {warning}")
    else:
        print("No obvious vulnerabilities found.")
