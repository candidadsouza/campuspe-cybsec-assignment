import socket
from datetime import datetime

# simple vulnerability database
vulnerabilities = {
    21: "FTP may allow anonymous login",
    22: "SSH may be vulnerable to brute force attacks",
    80: "HTTP may be vulnerable to XSS or SQL Injection",
    443: "HTTPS may have SSL/TLS issues"
}

# service names
services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

# get target IP
target = input("Enter target IP: ")

# report file name
date = datetime.now().strftime("%Y-%m-%d")
report_file = f"security_report_{target}_{date}.html"

# ports to scan
ports = [21, 22, 80, 443]

results = []

print("Starting scan...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

        service = services.get(port, "Unknown")
        issue = vulnerabilities.get(port, "No known issues")

        results.append((port, service, issue))

    sock.close()

# create html report
with open(report_file, "w") as file:
    file.write("<html><body>")
    file.write("<h1>Security Audit Report</h1>")
    file.write(f"<p>Target: {target}</p>")
    file.write("<table border='1'>")
    file.write("<tr><th>Port</th><th>Service</th><th>Possible Vulnerability</th></tr>")

    for port, service, issue in results:
        file.write(f"<tr><td>{port}</td><td>{service}</td><td>{issue}</td></tr>")

    file.write("</table>")
    file.write("</body></html>")

print(f"Report saved as {report_file}")
