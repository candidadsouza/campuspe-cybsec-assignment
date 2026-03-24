Bash Assignment – CampusPE Cybersecurity

Name: Candida D Souza

-----------------------------------
Questions Attempted:
Q1 – System Information Display
Q2 – File and Directory Manager
Q3 – Log File Analyzer
Q4 – Automated Backup Script
Q5 – User Account Reporter
-----------------------------------

Description:
This repository contains five Bash scripts that demonstrate:
- System information retrieval
- File and directory management
- Log file analysis
- Automated backup with timestamp and duration
- User account reporting and security checks

-----------------------------------
How to Run:

1. Make scripts executable:
   chmod +x *.sh

2. Run each script:
   ./q1_system_info.sh
   ./q2_file_manager.sh
   ./q3_log_analyzer.sh
   ./q4_backup.sh
   ./q5_user_report.sh

-----------------------------------
Sample Test Cases:

Q2:
- Created files and directories
- Renamed files
- Searched for files
- Counted files and directories

Q3:
- Used sample_log.txt
- Verified total entries, status codes, and top IP addresses

Q4:
- Created test_backup directory
- Performed compressed backup
- Verified timestamp, size, and duration

Q5:
- Generated user_report.txt
- Verified user statistics, group information, and security checks

-----------------------------------
Challenges Faced:

- Correctly parsing log file fields using awk (Q3)
- Recording interactive script outputs cleanly
- Implementing timestamp and duration calculation in Q4
- Extracting user and group information using awk and system files
