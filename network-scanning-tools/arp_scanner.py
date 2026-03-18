import subprocess  # To run system commands like 'arp -a'
import re          # For extracting IP and MAC using regex
import csv         # For exporting results to CSV file


# Function to get ARP table from system
def get_arp_table():
    try:
        # Run 'arp -a' command to get ARP table
        result = subprocess.run(
            ["arp", "-a"],
            capture_output=True,   # Capture output instead of printing
            text=True              # Convert output to string
        )
        return result.stdout       # Return command output

    except Exception as e:
        print("Error:", e)
        return None


# Function to extract IP and MAC addresses using regex
def parse_arp(output):

    # Pattern matches IP address + MAC address
    pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]{17})"

    # Find all matches in output
    matches = re.findall(pattern, output)

    return matches


# Function to display results in aligned table format
def display_results(entries):

    # Print table header
    print("\n{:<20} {:<20}".format("IP Address", "MAC Address"))
    print("-" * 40)

    # Print each IP and MAC pair
    for ip, mac in entries:
        print("{:<20} {:<20}".format(ip, mac))

    # Print total number of entries
    print(f"\nTotal entries: {len(entries)}")


# Function to save results to a text file
def save_to_file(entries):

    # Open file in write mode
    with open("arp_results.txt", "w") as f:

        # Write header
        f.write("{:<20} {:<20}\n".format("IP Address", "MAC Address"))
        f.write("-" * 40 + "\n")

        # Write each entry
        for ip, mac in entries:
            f.write("{:<20} {:<20}\n".format(ip, mac))

    print("Results saved to arp_results.txt")


# Function to export results to CSV file (bonus feature)
def export_to_csv(entries):

    # Open CSV file
    with open("arp_results.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write column headers
        writer.writerow(["IP Address", "MAC Address"])

        # Write each row
        for ip, mac in entries:
            writer.writerow([ip, mac])

    print("Results exported to arp_results.csv")


# Main program starts here
if __name__ == "__main__":

    print("=== ARP Scanner ===")
    print("Scanning ARP table...")

    # Get ARP output
    output = get_arp_table()

    if output:
        # Extract IP and MAC entries
        entries = parse_arp(output)

        # Display results on screen
        display_results(entries)

        # Ask user to save results to text file
        choice = input("\nSave results to file? (y/n): ")

        if choice.lower() == "y":
            save_to_file(entries)

        # Ask user to export results to CSV file
        csv_choice = input("Export results to CSV? (y/n): ")

        if csv_choice.lower() == "y":
            export_to_csv(entries)