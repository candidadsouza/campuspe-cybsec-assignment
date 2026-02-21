#!/bin/bash
# --------------------------------------------------
# Script Name: q2_file_manager.sh
# Description : Menu-driven File & Directory Manager
# --------------------------------------------------

while true
do
    echo "----------------------------------"
    echo "        FILE MANAGER MENU"
    echo "----------------------------------"
    echo "1. List files"
    echo "2. Create directory"
    echo "3. Create file"
    echo "4. Delete file"
    echo "5. Rename file"
    echo "6. Search files"
    echo "7. Count files and directories"
    echo "8. Exit"
    echo "----------------------------------"

    read -p "Enter your choice: " choice

    case $choice in

        1)
            echo "Files in current directory:"
            ls
            ;;

        2)
            read -p "Enter directory name: " dirname
            if [ -d "$dirname" ]; then
                echo "Directory already exists."
            else
                mkdir "$dirname" && echo "Directory created successfully."
            fi
            ;;

        3)
            read -p "Enter file name: " filename
            if [ -f "$filename" ]; then
                echo "File already exists."
            else
                touch "$filename" && echo "File created successfully."
            fi
            ;;

        4)
            read -p "Enter file name to delete: " filename
            if [ -f "$filename" ]; then
                rm "$filename" && echo "File deleted successfully."
            else
                echo "File does not exist."
            fi
            ;;

        5)
            read -p "Enter current file name: " oldname
            read -p "Enter new file name: " newname
            if [ -f "$oldname" ]; then
                mv "$oldname" "$newname" && echo "File renamed successfully."
            else
                echo "File does not exist."
            fi
            ;;

        6)
            read -p "Enter file name to search: " searchname
            find . -name "$searchname"
            ;;

        7)
            echo "Total files:"
            find . -type f | wc -l
            echo "Total directories:"
            find . -type d | wc -l
            ;;

        8)
            echo "Exiting program..."
            break
            ;;

        *)
            echo "Invalid choice. Please try again."
            ;;
    esac

    echo ""
done