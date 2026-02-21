#!/bin/bash
# Simple file and directory manager script

# Loop runs until user chooses to exit
while true
do

# Display menu
    echo "--------------------"
    echo "1. Create file"
    echo "2. Create directory"
    echo "3. Delete file"
    echo "4. Delete directory"
    echo "5. List files"
    echo "6. Open file"
    echo "7. Exit"
    echo "--------------------"

# Read user choice
    read -p "Enter choice: " ch

    # Create file and write content
    if [ "$ch" -eq 1 ]
    then
        echo "Create file selected"
        read -p "Enter file name: " f
        read -p "Enter text to write in file: " text
        echo "$text" > "$f"
        echo "File created with content"

    # Create directory
    elif [ "$ch" -eq 2 ]
    then
        echo "Create directory selected"
        read -p "Enter directory name: " d
        mkdir "$d"
        echo "Directory created"

    # Delete file
    elif [ "$ch" -eq 3 ]
    then
        echo "Delete file selected"
        read -p "Enter file name: " f
        rm "$f"
        echo "File deleted"

    # Delete directory
    elif [ "$ch" -eq 4 ]
    then
        echo "Delete directory selected"
        read -p "Enter directory name: " d
        rmdir "$d"
        echo "Directory deleted"

    # List files
    elif [ "$ch" -eq 5 ]
    then
        echo "Files in current folder:"
        ls

    # Open and display file content
    elif [ "$ch" -eq 6 ]
    then
        echo "Open file selected"
        read -p "Enter file name: " f
        echo "File content:"
        cat "$f"

    # Exit
    elif [ "$ch" -eq 7 ]
    then
        echo "Exiting program"
        break

    else
        echo "Wrong choice"
    fi

    echo ""
done