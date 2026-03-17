import subprocess   # Used to run system commands like nmap
import sys          # Used for system-related functions like exit()

# Function to check if Nmap is installed on the system
def check_nmap():
    try:
        # Try running 'nmap --version' to check availability
        subprocess.run(["nmap", "--version"], capture_output=True, text=True)
        return True   # If no error, Nmap is installed
    except FileNotFoundError:
        return False  # If error occurs, Nmap is not installed


# Function to run the selected Nmap scan
def run_scan(target, scan_type):

    # Decide which scan to perform based on user choice
    if scan_type == "1":
        print("\nPerforming: Host Discovery Scan (-sn)")  # Inform user
        command = ["nmap", "-sn", target]  # Command for host discovery

    elif scan_type == "2":
        print("\nPerforming: Default Port Scan (1-1000)")
        command = ["nmap", target]  # Default scan scans top ports

    elif scan_type == "3":
        ports = input("Enter port range (e.g., 1-100): ")  # Ask user for ports
        print(f"\nPerforming: Custom Port Scan (-p {ports})")
        command = ["nmap", "-p", ports, target]  # Custom port scan

    elif scan_type == "4":
        print("\nPerforming: Service Version Detection (-sV)")
        command = ["nmap", "-sV", target]  # Detect service versions

    elif scan_type == "5":
        print("\nPerforming: OS Detection (-O)")
        command = ["nmap", "-O", target]  # Detect operating system

    else:
        print("Invalid choice")  # If user enters wrong option
        return None

    try:
        print("\nScanning... please wait\n")  # Inform user scan started

        # Run the Nmap command
        result = subprocess.run(
            command,                 # Command to execute
            capture_output=True,     # Capture output instead of printing directly
            text=True,               # Convert output to string
            timeout=60               # Stop if scan takes more than 60 seconds
        )

        return result.stdout  # Return scan results

    except subprocess.TimeoutExpired:
        print("Scan timed out")  # Handle timeout error
        return None


# Function to save scan results into a file
def save_to_file(data):
    # Open file in write mode
    with open("nmap_results.txt", "w") as f:
        f.write(data)  # Write scan output to file

    print("Results saved to nmap_results.txt")  # Confirmation message


# Main program starts here
if __name__ == "__main__":

    print("=== Nmap Scanner ===")  # Title of program

    # Check if Nmap is installed before running
    if not check_nmap():
        print("Nmap is not installed!")  # Show error if not installed
        sys.exit()  # Stop the program

    print("Nmap is installed")  # Confirmation message

    # Ask user to enter target IP or network
    target = input("Enter target IP or network: ")

    # Display scan options menu
    print("\nSelect scan type:")
    print("1. Host Discovery (-sn)")
    print("2. Port Scan (1-1000)")
    print("3. Custom Port Scan")
    print("4. Service Version Detection (-sV)")
    print("5. OS Detection (-O)")

    # Get user choice
    choice = input("Enter choice (1-5): ")

    # Run the selected scan
    output = run_scan(target, choice)

    # If scan produced output
    if output:
        print(f"\nTarget: {target}")  # Show target
        print("\nScan Results:\n")
        print("=" * 50)  # Divider line
        print(output)    # Print scan results
        print("=" * 50)

        # Ask user if they want to save results
        save = input("\nSave results to file? (y/n): ")

        # If user chooses yes, save results
        if save.lower() == "y":
            save_to_file(output)