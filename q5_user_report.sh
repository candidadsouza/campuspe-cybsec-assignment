#!/bin/bash
# q5_user_report.sh
# User Account Reporting Script

echo "-----------------------------------"
echo "         USER ACCOUNT REPORT"
echo "-----------------------------------"

report="user_report.txt"

{
echo "1. USER STATISTICS"
echo "-------------------"

# Total users
total_users=$(wc -l < /etc/passwd)
echo "Total Users: $total_users"

# System users (UID < 1000)
system_users=$(awk -F: '$3 < 1000 {print $1}' /etc/passwd | wc -l)
echo "System Users (UID < 1000): $system_users"

# Regular users (UID >= 1000)
regular_users=$(awk -F: '$3 >= 1000 {print $1}' /etc/passwd | wc -l)
echo "Regular Users (UID >= 1000): $regular_users"

# Logged-in users
echo ""
echo "Currently Logged-in Users:"
who

echo ""
echo "2. USER DETAILS"
echo "-------------------"

# Username, UID, Home, Shell
awk -F: '{print "Username:", $1, "| UID:", $3, "| Home:", $6, "| Shell:", $7}' /etc/passwd

echo ""
echo "3. GROUP INFORMATION"
echo "-------------------"

# List all groups
echo "All Groups:"
cut -d: -f1 /etc/group

echo ""
echo "Group Member Counts:"
awk -F: '{print $1, "->", split($4,a,","), "members"}' /etc/group

echo ""
echo "4. SECURITY CHECK"
echo "-------------------"

# Users with UID 0
echo "Users with UID 0:"
awk -F: '$3 == 0 {print $1}' /etc/passwd

# Users without passwords (empty password field)
echo ""
echo "Users without password (check /etc/shadow may require root):"
awk -F: '$2 == "" {print $1}' /etc/passwd

echo ""

} > "$report"

echo "Report saved as $report"
echo "-----------------------------------"
echo "User report completed"