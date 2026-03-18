import subprocess   # To run system commands like nmap
import sys          # To exit program if needed
import csv          # For exporting results to CSV
import re           # For parsing output


# Function to check if Nmap is installed
def check_nmap():
    try:
        subprocess.run(["nmap", "--version"], capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False


# Function to run selected Nmap scan
def run_scan(target, scan_type):

    if scan_type == "1":
        print("\nPerforming: Host Discovery Scan (-sn)")
        command = ["nmap", "-sn", target]

    elif scan_type == "2":
        print("\nPerforming: Default Port Scan (1-1000)")
        command = ["nmap", target]

    elif scan_type == "3":
        ports = input("Enter port range (e.g., 1-100): ")
        print(f"\nPerforming: Custom Port Scan (-p {ports})")
        command = ["nmap", "-p", ports, target]

    elif scan_type == "4":
        print("\nPerforming: Service Version Detection (-sV)")
        command = ["nmap", "-sV", target]

    elif scan_type == "5":
        print("\nPerforming: OS Detection (-O)")
        command = ["nmap", "-O", target]

    else:
        print("Invalid choice")
        return None

    try:
        print("\nScanning... please wait\n")

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=60
        )

        return result.stdout

    except subprocess.TimeoutExpired:
        print("Scan timed out")
        return None


# Function to save results to a text file
def save_to_file(data):

    with open("nmap_results.txt", "w") as f:
        f.write(data)

    print("Results saved to nmap_results.txt")


# ⭐ Improved CSV export with structured data
def export_to_csv(data, target):

    with open("nmap_results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write general info
        writer.writerow(["Target", target])
        writer.writerow([])

        # Extract scan time
        time_match = re.search(r"scanned in (.+)", data)
        if time_match:
            writer.writerow(["Scan Time", time_match.group(1)])
            writer.writerow([])

        # Table header
        writer.writerow(["Port", "State", "Service"])

        lines = data.split("\n")

        for line in lines:
            match = re.match(r"(\d+)/tcp\s+(\w+)\s+(.+)", line)

            if match:
                port = match.group(1)
                state = match.group(2)
                service = match.group(3)

                writer.writerow([port, state, service])

    print("Results exported to formatted nmap_results.csv")


# Main program
if __name__ == "__main__":

    print("=== Nmap Scanner ===")

    if not check_nmap():
        print("Nmap is not installed!")
        sys.exit()

    print("Nmap is installed")

    target = input("Enter target IP or network: ")

    print("\nSelect scan type:")
    print("1. Host Discovery (-sn)")
    print("2. Port Scan (1-1000)")
    print("3. Custom Port Scan")
    print("4. Service Version Detection (-sV)")
    print("5. OS Detection (-O)")

    choice = input("Enter choice (1-5): ")

    output = run_scan(target, choice)

    if output:
        print(f"\nTarget: {target}")
        print("\nScan Results:\n")
        print("=" * 50)
        print(output)
        print("=" * 50)

        # Save to text file
        save = input("\nSave results to file? (y/n): ")

        if save.lower() == "y":
            save_to_file(output)

        # Export to CSV
        csv_choice = input("Export results to CSV? (y/n): ")

        if csv_choice.lower() == "y":
            export_to_csv(output, target)