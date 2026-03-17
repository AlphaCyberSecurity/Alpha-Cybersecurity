import socket
import subprocess
import platform
from datetime import datetime

# MAC address manufacturer prefixes
# First 6 characters of MAC = manufacturer
MAC_VENDORS = {
    "00:50:56": "VMware",
    "00:0C:29": "VMware",
    "00:1A:11": "Google",
    "00:1C:B3": "Apple",
    "00:26:BB": "Apple",
    "3C:D0:F8": "Apple",
    "A4:C3:F0": "Apple",
    "F0:DB:F8": "Apple",
    "DC:A4:CA": "Apple",
    "B8:27:EB": "Raspberry Pi",
    "DC:A6:32": "Raspberry Pi",
    "00:14:22": "Dell",
    "00:21:70": "Dell",
    "18:03:73": "Dell",
    "00:23:AE": "Dell",
    "00:1B:21": "Intel",
    "00:1F:3B": "Intel",
    "8C:8D:28": "Intel",
    "00:15:5D": "Microsoft Hyper-V",
    "00:50:F2": "Microsoft",
    "28:D2:44": "Microsoft",
    "00:17:FA": "Microsoft",
    "00:1D:7E": "Cisco",
    "00:1E:F7": "Cisco",
    "00:24:14": "Cisco",
    "CC:46:D6": "Cisco",
    "00:09:0F": "Fortinet",
    "00:0F:DE": "Huawei",
    "00:18:82": "Huawei",
    "54:89:98": "Huawei",
    "00:25:9C": "Cisco/Linksys",
    "20:AA:4B": "Xiaomi",
    "64:09:80": "Xiaomi",
    "F8:A4:5F": "Samsung",
    "00:16:32": "Samsing",
    "8C:77:12": "Samsung",
    "18:29:5E": "Samsung",
    "00:1C:62": "Samsung",
    "94:35:0A": "Sony",
    "00:01:4A": "Sony",
    "00:24:BE": "Nintendo",
    "00:09:BF": "Nintendo",
    "98:41:5C": "TP-Link",
    "50:C7:BF": "TP-Link",
    "14:CC:20": "TP-Link",
    "C0:4A:00": "TP-Link",
    "00:0A:EB": "TP-Link",
    "10:FE:ED": "TP-Link",
    "00:1A:92": "ASUS",
    "00:1D:0F": "ASUS",
    "04:D4:C4": "ASUS",
    "BC:EE:7B": "ASUS",
    "00:E0:4C": "Realtek",
    "00:26:18": "HP",
    "00:21:5A": "HP",
    "3C:A8:2A": "HP",
    "00:17:08": "HP",
    "00:1B:63": "Apple AirPort",
    "00:23:12": "Apple AirPort",
    }

def get_mac_windows(ip):
    try:
        #Rum ARP to get MAC address on Windows 
        output = subprocess.check_output(
            f"arp -a {ip}",
            shell=True,
            stderr=subprocess.DEVNULL
        ).decode()
    # Find MAC address pattern in output
        mac_pattern = r"([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}"
        match = re.search(mac_pattern, output)
        if match:
            return match.group(0).upper().replace("-", ":")
    except:
        return None
    
def get_mac_unix(ip):
    try:
        # Ping first to populate ARP cache
        subprocess.call(
            ["ping", "-c", "1", "-w", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        output = subprocess.check_output(
            ["arp", "n", ip],
            stderr=subprocess.DEVNULL
        ).decode()
        mac_pattern = r"([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}"
        match = re.search(mac_pattern, output)
        if match:
            return match.group(0).upper()
        return None
    except:
        return None

def get_mac(ip):
    if platform.system().lower() == "windows":
        return get_mac_windows(ip)
    else:
        return get_mac_unix(ip)

def get_manufacturer(mac):
    if not mac:
        return "Unknown Manufacturer"
    #Check first 8 characters (XX:XX:XX)
    prefix = mac[:8].upper()
    if prefix in MAC_VENDORS:
        return MAC_VENDORS[prefix]
    #Check first 6 characters wihtout last pair
    prefix6 = mac[:6].upper().replace(":", "")
    for vendor_mac, vendor_name in MAC_VENDORS.items():
        if vendor_mac.replace(":", "") == prefix6:
            return vendor_name
    return "Unknown Manufacturer"

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return None
    
def ping_host(ip):
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    cmd = ["ping", flag, "1", "-w", "500", ip] if platform.system().lower() == "windows" else ["ping", flag, "1", "-w", "1", ip]
    result = subprocess.call(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result == 0
def scan_network(base_ip):
    print("\n" + "=" * 60)
    print("   ALPHA CYBERSECURITY - NETWORK SCANNER")
    print("   Time:", datetime.now().strf("%Y-%m-%d %H:%M"))
    print("   Scanning:", base_ip + ".1 to .50")
    print("=" * 60)
    print(f"\n {'IP ADDRESS':<18}{'MAC ADDRESS':<20}{'Manufacturer':<22}{'HOSTNAME'}")
    print(" " + "-" * 80)

    found = []
    unknown_count = 0

    for i in range(1, 51):
        ip = base_ip + "." + str(i)
        if ping_host(ip):
            mac = get_mac(ip)
            manufacturer = get_manufacturer(mac)
            hostname = get_hostname(ip) or "Unknown Device"
            mac_display = mac if mac else "Could not retrieve"

            found.append({
                "ip": ip,
                "mac": mac_display,
                "manufactuer": manufacturer,
                "hostname": hostname
            })

            #Flag unknown manufacturers
            flag = "  <- INVESTIGATE" if manufacturer == "Unknown Manufacturer" else ""
            print(f"  {ip:<18}{mac_display:<20}{manufacturer:<22}{hostname}{flag}")

            if manufacturer == "Unknown Manufacturer":
                unknown_count += 1
    print("\n" + "=" * 60)
    print(f"  TOTAL DEVICES FOUND:          {len(found)}")
    print(f"  IDENTIFIED MANUFACTURER:      {len(found) - unknown_count}")
    print(F"  UNKNOWN DEVICES:              {unknown_count}")
    print("=" * 60)

    if unknown_count > 0:
        print(f"\n WARNING: {unknown_count} device(s) could not be identified.")
        print("  Cross-check these with your router's device list.")
        print("  Any device you do not recogise is a security risk.")
    print("\n HOW TO IDENTIFY UNKNOWN DEVICES:")
    print("  1. Open your browser")
    print("  2. Got to your router IP e.g. 192.168.1.1")
    print("  3. Log in and find 'Connected Devices' or DHCP Clients'")
    print("  4. Your router shows the actual devices name\n")

    return found

#CHANGE THIS to match your network
#If your router is 192.168.1.1 use "192.168.1"
#If your router is 192.168.0.1 use "192.168.0"
YOUR_NETWORK = "192.168.0"

scan_network(YOUR_NETWORK)