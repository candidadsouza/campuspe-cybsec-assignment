#!/bin/bash
# Simple user account report (beginner friendly)

echo "USER ACCOUNT REPORT"
echo "------------------"

# 1. Show currently logged-in users
echo "Currently logged-in users:"
who
echo ""

# 2. List all local users from /etc/passwd
echo "All local users:"
cat /etc/passwd
echo ""

# 3. List only real users (those with home directories under /home)
echo "Real users (with /home directories):"
cat /etc/passwd | grep '/home' | cut -d: -f1
echo ""



# Save report to a file
report="user_report.txt"
{
  echo "Currently logged-in users:"; who; echo ""
  echo "All local users:"; cat /etc/passwd; echo ""
  echo "Real users:"; cat /etc/passwd | grep '/home' | cut -d: -f1; echo ""
} > $report

echo "Report saved as $report"