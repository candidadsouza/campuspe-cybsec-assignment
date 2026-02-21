#!/bin/bash
# --------------------------------------------------
# Script Name: q1_system_info.sh
# Description : Displays essential system information
# Author      : Your Name
# --------------------------------------------------

# Print formatted heading
echo "=============================="
echo "       SYSTEM INFORMATION"
echo "=============================="

# Store required system information into variables

# Get current logged-in username
USERNAME=$(whoami)

# Get system hostname
HOSTNAME=$(hostname)

# Get current date and time
CURRENT_DATE=$(date)

# Get operating system name (Linux, Darwin, etc.)
OS_NAME=$(uname -s)

# Get present working directory
CURRENT_DIR=$(pwd)

# Get user's home directory
HOME_DIR=$HOME

# Count number of currently logged-in users
LOGGED_USERS_COUNT=$(who | wc -l)

# Get system uptime information
SYSTEM_UPTIME=$(uptime)

# Display collected information in formatted output
echo "Username            : $USERNAME"
echo "Hostname            : $HOSTNAME"
echo "Date & Time         : $CURRENT_DATE"
echo "Operating System    : $OS_NAME"
echo "Current Directory   : $CURRENT_DIR"
echo "Home Directory      : $HOME_DIR"
echo "Logged-in Users     : $LOGGED_USERS_COUNT"
echo "System Uptime       : $SYSTEM_UPTIME"

echo ""


