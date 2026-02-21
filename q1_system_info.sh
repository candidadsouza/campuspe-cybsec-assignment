#!/bin/bash
# -----------------------------------------
# Script Name : q1_system_info.sh
# Description : Displays basic system information
# -----------------------------------------

# Print main heading
echo "SYSTEM INFORMATION"
echo "==================="

# Display the system (host) name
echo "System Name:"
uname -n
echo ""

# Display detailed system information such as OS and kernel version
echo "Detailed System Information:"
uname -a
echo ""

# Display how long the system has been running
echo "System Uptime:"
uptime
echo ""

# Display memory usage including RAM and swap
echo "Memory Usage:"
free
echo ""

# Display disk space usage of file systems
echo "Disk Usage:"
df
echo ""

# Display the current logged-in user
echo "Current Logged-in User:"
whoami
echo ""

# Display current date and time
echo "Current Date and Time:"
date
echo ""

# Display list of all users currently logged into the system
echo "Logged-in Users:"
who
echo ""

# Display the present working directory
echo "Current Working Directory:"
pwd
echo ""

