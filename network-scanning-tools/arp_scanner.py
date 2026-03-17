import subprocess
import re

# Function to get ARP table
def get_arp_table():
    try:
        # Run arp command
        result = subprocess.run(
            ["arp", "-a"],
            capture_output=True,
            text=True
        )
        return result.stdout

    except Exception as e:
        print("Error:", e)
        return None


# Function to parse ARP output and extract IP + MAC
def parse_arp(output):

    # Regex to match IP and MAC address
    pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]{17})"

    matches = re.findall(pattern, output)

    return matches


# Function to display results nicely (FIXED ALIGNMENT)
def display_results(entries):

    # Proper column spacing using formatting
    print("\n{:<20} {:<20}".format("IP Address", "MAC Address"))
    print("-" * 40)

    for ip, mac in entries:
        print("{:<20} {:<20}".format(ip, mac))

    print(f"\nTotal entries: {len(entries)}")


# Function to save results to file
def save_to_file(entries):

    with open("arp_results.txt", "w") as f:
        f.write("{:<20} {:<20}\n".format("IP Address", "MAC Address"))
        f.write("-" * 40 + "\n")

        for ip, mac in entries:
            f.write("{:<20} {:<20}\n".format(ip, mac))

    print("Results saved to arp_results.txt")


# Main program
if __name__ == "__main__":

    print("=== ARP Scanner ===")
    print("Scanning ARP table...")

    output = get_arp_table()

    if output:
        entries = parse_arp(output)

        display_results(entries)

        # Ask user if they want to save results
        choice = input("\nSave results to file? (y/n): ")

        if choice.lower() == "y":
            save_to_file(entries)