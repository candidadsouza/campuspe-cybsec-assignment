#!/bin/bash
# Log analysis script using basic commands

echo "----------------------"
echo "LOG ANALYSIS"
echo "----------------------"

# Step 1: Ask for log file name
read -p "Enter log file name: " logfile

# Step 2: Display log file contents
echo "Displaying log file:"
cat "$logfile"

# Step 3: Search for WARNING messages
echo "WARNING messages:"
grep "WARNING" "$logfile"

# Step 4: Search for failed login attempts
echo "Failed login attempts:"
grep "failed login" "$logfile"

# Step 5: Count failed entries
failed_count=$(grep -c "failed" "$logfile")
echo "Number of failed entries: $failed_count"

# Step 6: Extract IP addresses from logs
echo "IP addresses found:"
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' "$logfile"

# Step 7: Create incident report
echo "Creating incident report..."

echo "Incident Report" > incident_report.txt
echo "----------------" >> incident_report.txt
echo "Warnings found:" >> incident_report.txt
grep "WARNING" "$logfile" >> incident_report.txt
echo "" >> incident_report.txt

echo "Failed login attempts:" >> incident_report.txt
grep "failed login" "$logfile" >> incident_report.txt
echo "" >> incident_report.txt

echo "Number of failed entries: $failed_count" >> incident_report.txt
echo "" >> incident_report.txt

echo "IP addresses detected:" >> incident_report.txt
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' "$logfile" >> incident_report.txt

# Step 8: Display incident report
echo "Incident report contents:"
cat incident_report.txt

echo "----------------------"
echo "Log analysis completed"