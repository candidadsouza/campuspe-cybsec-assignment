import subprocess
import platform
import re

# This function sends a ping request to a host (IP or domain name)
def ping_host(host):

    # Detect the operating system to choose the correct ping parameter
    # Windows uses "-n", Linux/Mac use "-c"
    param = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        # Run the ping command using subprocess
        result = subprocess.run(
            ["ping", param, "4", host],   # Ping the host 4 times
            capture_output=True,         # Capture the output of the command
            text=True,                   # Return output as text instead of bytes
            timeout=10                   # Stop if the command takes more than 10 seconds
        )

        # If return code is 0, the host is reachable
        if result.returncode == 0:
            print(f"\nHost: {host}")
            print("Status: Reachable")

            # Use regex to find the average response time from ping output
            match = re.search(r"Average = (\d+)ms", result.stdout)

            # If a match is found, print the average time
            if match:
                print(f"Average Time: {match.group(1)} ms")

        else:
            # If return code is not 0, the host is unreachable
            print(f"\nHost: {host}")
            print("Status: Unreachable")

    # Handle timeout error
    except subprocess.TimeoutExpired:
        print("Ping request timed out")


# Main program starts here
if __name__ == "__main__":

    print("=== Ping Scanner ===")

    # Ask the user if they want to ping multiple hosts
    choice = input("Ping multiple hosts? (y/n): ")

    # If user chooses multiple hosts
    if choice.lower() == "y":

        # User enters hosts separated by commas
        hosts = input("Enter hosts separated by comma: ").split(",")

        # Loop through each host and ping it
        for host in hosts:
            ping_host(host.strip())

    else:
        # If user chooses single host
        host = input("Enter hostname or IP: ")

        # Ping the single host
        ping_host(host)