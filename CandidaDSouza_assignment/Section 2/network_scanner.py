import socket
import time

# take input
target = input("Enter IP: ")
ports = input("Enter ports (comma separated): ")

# convert ports to list
port_list = ports.split(",")

start_time = time.time()

file = open("scan_results.txt", "w")
file.write("Scanning " + target + "\n")

# scan ports
for port in port_list:
    port = int(port.strip())
    
    s = socket.socket()
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} OPEN")
        file.write(f"Port {port} OPEN\n")
    else:
        print(f"Port {port} CLOSED")
        file.write(f"Port {port} CLOSED\n")
    
    s.close()

end_time = time.time()

print("\nScan complete")
print("Time taken:", round(end_time - start_time, 2), "seconds")

file.write("Scan complete\n")
file.write("Time taken: " + str(round(end_time - start_time, 2)) + " seconds\n")

file.close()
