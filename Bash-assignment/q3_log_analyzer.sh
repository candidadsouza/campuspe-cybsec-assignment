#!/bin/bash
# q3_log_analyzer.sh
# Simple Web Server Log Analyzer

echo "-----------------------------------"
echo "         LOG FILE ANALYZER"
echo "-----------------------------------"

# Ask user for log file name
read -p "Enter log file name: " logfile

# Check if file exists
if [ ! -f "$logfile" ]; then
    echo "Error: File does not exist."
    exit 1
fi

echo ""

# Total number of log entries
echo "Total Log Entries:"
wc -l < "$logfile"

echo ""

# Number of unique IP addresses (column 1)
echo "Unique IP Addresses:"
awk '{print $1}' "$logfile" | sort | uniq | wc -l

echo ""

# Count HTTP status codes (column 7)
echo "Status Code Counts:"
awk '{print $7}' "$logfile" | sort | uniq -c

echo ""

# Most frequently requested page (column 6)
echo "Most Frequently Requested Page:"
awk '{print $6}' "$logfile" | sed 's/"//g' | sort | uniq -c | sort -nr | head -1

echo ""

# Top 3 IP addresses by request count
echo "Top 3 IP Addresses:"
awk '{print $1}' "$logfile" | sort | uniq -c | sort -nr | head -3

echo ""
echo "-----------------------------------"
echo "Log Analysis Completed"