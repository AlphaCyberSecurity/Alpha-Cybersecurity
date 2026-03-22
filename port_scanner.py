import socket
from datetime import datetime
#ALPHA CYBERSECURITY - PORT SCANNER

#Common ports, what they do, and their risks
PORTS = {
    21: ("FTP - File transfer", "HIGH", "Unencrypted file transfer. Often exploited."),
    22: ("SSH - Remote Access", "MEDIUM", "Secure remote access. Fineif you need it, risky if you do not."),
    23: ("Telnet - Remote Access", "CRITICAL", "Completely unencrypted. Should never be open."),
    25: ("SMTP - Email sending", "MEDIUM", "Email server port. Unusual on home networks."),
    53: ("DNS - Domain Look up", "LOW", "Noraml on routers. Unusual on other devices."),
    80: ("HTTP - Web Server", "MEDIUM", "Unencrypted web traffic. Could expose a web interface."),
    110: ("POP3 - Email", "MEDIUM", "Old email protocol. Should use encrypted version."),
    135: ("RPC - Windows", "HIGH", "Windows remote procedure calls. Common attack target."),
    139: ("NetBIOS - Windows", "HIGH", "Old Window file sharing. Frequently exploited."),
    143: ("IMAP - Email", "MEDIUM", "Email access protocol."),
    443: ("HTTPS - Secure Web", "LOW", "Encrypted web traffic. Normal and expected."),
    445: ("SMB - File Sharing", "CRITICAL", "Major ransomware target. Should be closed on home networks."),
    1433: ("MSSQL - Database", "HIGH", "Microsoft database. Should never be exposed externally."),
    3306: ("MySQL - Database", "HIGH", "Database port. Should never be exposed externally."),
    3389: ("RDP - Remote Desktop", "CRITICAL", "Most attacked port on the internal. Close immediately if not needed."),
    5900: ("VNC - Remote Desktop", "HIGH", "Remote desktop protocol. Often poorly secured."),
    8080: ("HTTP Alt - Web", "MEDIUM", "Alternate web port. Could be an admin panel."),
    8443: ("HTTPS Alt - Web", "LOW", "Alternative secure web port."),
    27017: ("MongoDB - Database", "HIGH", "Database port. Has caused massive data breaches when exposed."),
}

RISK_ICON = {
    "LOW": "[LOW]",
    "MEDIUM": "[MEDIUM]",
    "HIGH": "[HIGH]",
    "CRITICAL": "[CRITICAL]",
}

def scan_port(host, port, timeout=0.5):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except Exception:
        return False
    
def get_risk_summary(open_ports):
    critical = [p for p in open_ports if PORTS.get(p, ("", "LOW", ""))[1] == "CRITICAL"]
    high = [p for p in open_ports if PORTS.get(p, ("", "LOW", ""))[1] == "HIGH"]
    return critical, high

def scan_host(host):
    print("\n" + "=" * 60)
    print(" ALPHA CYBERSECURITY - PORT SCANNER")
    print(f" Target: {host}")
    print(f" Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print(f"\n Scanning {len(PORTS)} common ports...\n")

    open_ports = []
    for port in sorted(PORTS.key()):
        if scan_port(host, port):
            service, risk, explanation = PORTS[port]
            icon = RISK_ICON[risk]
            open_ports.append(port)
            print(f" {icon} OPEN Port{str(port):<6}{service}")
            print(f" Risk: {risk} - {explanation}\n")
    print("=" * 60)
    print(f" SCAN COMPLETE")
    print(f" Open ports found: {len(open_ports)}")

    if open_ports:
        critical, high = get_risk_summary(open_ports)

        if critical:
            print(f"\n CRITICAL PORTS OPEN: {len(critical)}")
            print(" These must be closed immediately:")
            for p in critical:
                print(f" -> Port {p}: {PORTS[p][0]}")

        if high:
            print(f"\n HIGH RISK PORTS OPEN: {len(high)}")
            print(" Investigate these urgently:")
            for p in high:
                print(f" -> Port: {p}: {PORTS[p][0]}")
            
        if not critical and not high:
            print("\n No critical or high risk ports found.")
            print(" Keep monitoring regularly.")
        else:
            print("\n No open ports detected on common ports.")
            print(" This device appears well secured.")
        
        print("\n LEGAL REMINDER: Only scan devices you own or")
        print(" have written permission to test.")
        print("=" * 60 + "\n")

        return open_ports
    
#MAIN
print("=" * 60)
print(" ALPHA CYBERSECURITY - PORT SCANNER")
print("=" * 60)
print(" Scans a device for open ports and security risks.")
print(" Only scan device you own!\n")

while True:
    target = input(" Enter IP address to scan (or quit): ").strip()
    if target.lower() == "quit":
        print("\n Scanner closed. Stay Secure.")
        break
    if not target:
        continue
    scan_host(target)
    again = input(" Scan another device? (yes/no): ").strip().lower()
    if again == "no":
        print("\n Scanner closed. Stay secure.")
        break