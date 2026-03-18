# Network Scanning Automation

## Project Description

This project automates basic network scanning tools using Python.
It includes four tools:

* Ping Scanner
* ARP Scanner
* Nmap Scanner
* Unified Network Scanner (Bonus)

These tools help in performing network reconnaissance and understanding network behavior using Python.



## Requirements

* Python 3.6 or higher
* Nmap installed



## How to Install Nmap

### Windows

Download from: https://nmap.org/download.html

### Linux

sudo apt-get install nmap

### Mac

brew install nmap



## How to Run the Programs

### 1. Ping Scanner

Run:
python ping_scanner.py

Example:
Enter hostname or IP: google.com



### 2. ARP Scanner

Run:
python arp_scanner.py



### 3. Nmap Scanner

Run:
python nmap_scanner.py

Example:
Enter target IP or network: 127.0.0.1
Select scan type: 2



### 4. Unified Network Scanner (Bonus)

Run:
python network_scanner.py

This tool combines:

* Ping Scanner
* ARP Scanner
* Nmap Scanner

All functionalities are accessible through a single menu-driven interface.



## Features

* Cross-platform support (Windows, Linux, Mac)
* Multiple scan options (Nmap)
* Output parsing using regular expressions
* Save results to file
* Export results to CSV format (Bonus)
* Unified scanner combining all tools (Bonus)
* Error handling



## Screenshots

Screenshots are available in the `screenshots` folder:

* ping_output.png
* arp_output.png
* nmap_output.png



## Project Structure

network-scanning-tools
ping_scanner.py
arp_scanner.py
nmap_scanner.py
network_scanner.py
README.md
screenshots
  ping_output.png
  arp_output.png
  nmap_output.png



## Important Notes

* Only scan networks you own or have permission to scan
* Unauthorized network scanning is illegal
* Use these tools only for educational purposes



## Author

Candida D Souza
