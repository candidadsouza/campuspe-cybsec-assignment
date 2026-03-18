import subprocess
import platform
import re
import csv
import sys


# ---------------- PING SCANNER ----------------
def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", param, "4", host],
            capture_output=True,
            text=True,
            timeout=10
        )

        if result.returncode == 0:
            print(f"\nHost: {host} → Reachable")

            match = re.search(r"Average = (\d+)ms", result.stdout)
            if match:
                print(f"Average Time: {match.group(1)} ms")
        else:
            print(f"\nHost: {host} → Unreachable")

    except:
        print("Ping failed")


# ---------------- ARP SCANNER ----------------
def arp_scan():
    result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    output = result.stdout

    pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]{17})"
    entries = re.findall(pattern, output)

    print("\n{:<20} {:<20}".format("IP Address", "MAC Address"))
    print("-" * 40)

    for ip, mac in entries:
        print("{:<20} {:<20}".format(ip, mac))

    print(f"\nTotal entries: {len(entries)}")


# ---------------- NMAP SCANNER ----------------
def nmap_scan():
    target = input("Enter target IP: ")

    print("\n1. Host Discovery")
    print("2. Port Scan")
    print("3. Service Detection")

    choice = input("Enter choice: ")

    if choice == "1":
        cmd = ["nmap", "-sn", target]
    elif choice == "2":
        cmd = ["nmap", target]
    elif choice == "3":
        cmd = ["nmap", "-sV", target]
    else:
        print("Invalid choice")
        return

    print("\nScanning...\n")

    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout

    print(output)

    # Optional CSV export
    save = input("Export results to CSV? (y/n): ")

    if save.lower() == "y":
        export_nmap_csv(output, target)


def export_nmap_csv(data, target):
    with open("unified_nmap.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Target", target])
        writer.writerow([])

        writer.writerow(["Port", "State", "Service"])

        for line in data.split("\n"):
            match = re.match(r"(\d+)/tcp\s+(\w+)\s+(.+)", line)
            if match:
                writer.writerow([match.group(1), match.group(2), match.group(3)])

    print("CSV exported as unified_nmap.csv")


# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("\n=== Unified Network Scanner ===")
        print("1. Ping Scanner")
        print("2. ARP Scanner")
        print("3. Nmap Scanner")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            host = input("Enter IP/Host: ")
            ping_host(host)

        elif choice == "2":
            arp_scan()

        elif choice == "3":
            nmap_scan()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# Run program
if __name__ == "__main__":
    main()