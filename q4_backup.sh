#!/bin/bash
# Simple backup script with timestamp

echo "----------------------"
echo "BACKUP SCRIPT"
echo "----------------------"

# Ask user for source directory
read -p "Enter directory to backup: " src

# Check if source directory exists
if [ ! -d "$src" ]
then
    echo "Source directory not found"
    exit 1
fi

# Create backup directory if it does not exist
backup_dir="backup"
mkdir -p "$backup_dir"

# Get current date and time
time=$(date +"%Y%m%d_%H%M%S")

# Backup file name with timestamp
backup_file="$backup_dir/backup_$time.tar"

# Create backup using tar
tar -cf "$backup_file" "$src"

echo "Backup created successfully"
echo "Backup file: $backup_file"