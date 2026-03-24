#!/bin/bash
# q4_backup.sh
# Automated Backup Script with Timestamp

echo "----------------------"
echo "     BACKUP SCRIPT"
echo "----------------------"

# Ask for source directory
read -p "Enter directory to backup: " src

# Check if source exists
if [ ! -d "$src" ]; then
    echo "Source directory not found."
    exit 1
fi

# Ask for destination directory
read -p "Enter destination directory: " dest

# Create destination directory if needed
mkdir -p "$dest"

# Ask backup type
echo "Choose backup type:"
echo "1. Simple Copy"
echo "2. Compressed Archive (tar.gz)"
read -p "Enter choice (1 or 2): " choice

# Generate timestamp
timestamp=$(date +"%Y%m%d_%H%M%S")

# Record start time
start_time=$(date +%s)

if [ "$choice" -eq 1 ]; then
    backup_path="$dest/backup_$timestamp"
    cp -r "$src" "$backup_path"
elif [ "$choice" -eq 2 ]; then
    backup_path="$dest/backup_$timestamp.tar.gz"
    tar -czf "$backup_path" "$src"
else
    echo "Invalid choice."
    exit 1
fi

# Record end time
end_time=$(date +%s)

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "Backup created successfully."
    echo "Backup location: $backup_path"

    # Display backup size
    echo "Backup size:"
    du -h "$backup_path"

    # Calculate duration
    duration=$((end_time - start_time))
    echo "Backup completed in $duration seconds."
else
    echo "Backup failed."
fi