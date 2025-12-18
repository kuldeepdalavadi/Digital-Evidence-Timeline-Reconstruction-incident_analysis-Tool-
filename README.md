# Digital-Evidence-Timeline-Reconstruction-incident_analysis-Tool-
**Digital Evidence Timeline Reconstruction Incident Analysis Tool** collects system and authentication logs, preserves their integrity using hashing, and reconstructs events in chronological order. It helps investigators analyze incident sequences, detect suspicious activities, and support accurate digital forensic investigations.
Digital Evidence Timeline Reconstruction – Incident Analysis Tool

 📌 Project Description

The **Digital Evidence Timeline Reconstruction – Incident Analysis Tool** is a forensic utility designed to collect, preserve, and analyze digital evidence from system and authentication logs. The tool reconstructs events in chronological order to help investigators understand incident sequences, detect suspicious activities, and support digital forensic investigations while maintaining evidence integrity.

🎯 Objectives

* Collect system and authentication logs
* Preserve evidence integrity using cryptographic hashing (SHA-256)
* Parse and normalize timestamps
* Reconstruct a chronological timeline of events
* Support incident analysis and forensic reporting

🛠 Tools & Technologies

* **Operating System:** Kali Linux
* **Programming Language:** Python 3
* **Forensic Techniques:** Log analysis, hashing, timeline reconstruction
* **Utilities:** sha256sum, Git, GitHub

📥 Installation

Follow these steps to install and prepare the tool on Kali Linux:

bash
sudo apt update
sudo apt install python3 git -y

Clone the project repository:
bash
git clone https://github.com/USERNAME/Digital-Evidence-Timeline-Reconstruction.git
cd Digital-Evidence-Timeline-Reconstruction

Ensure Python is installed:
bash
python3 --version

 📂 Project Structure
Timeline_Project/
 ├── evidence/
 │    ├── auth.log
 │    ├── syslog
 │    ├── auth.log.hash
 │    └── syslog.hash
 ├── scripts/
 │    └── timeline.py
 ├── output/
 │    └── timeline.txt
 └── README.md

 ⚙️ Implementation Steps

 1. Log Collection

System and authentication logs are collected from the Linux system and stored in the `evidence/` directory.

 2. Evidence Integrity

SHA-256 hash values are generated for each log file to ensure integrity and prevent tampering.

3. Timeline Reconstruction

A Python script parses log files, extracts timestamps, and sorts events in chronological order.

 4. Output Generation

The reconstructed timeline is saved as a text file for analysis and reporting.

▶️ How to Run the Tool

bash
cd scripts
python3 timeline.py

 📊 Sample Output

Dec 18 09:15:01 – Failed login attempt detected
Dec 18 09:18:22 – Successful user login

## 🔐 Forensic Integrity

* Evidence files are preserved in read-only format
* Hash verification ensures authenticity
* Suitable for academic and investigative use

## 📈 Applications

* Cybercrime investigation
* Incident response
* Digital forensics education
* Log-based security analysis

 🚀 Future Enhancements

* GUI-based interface
* AI-based anomaly detection
* Support for additional log sources
* Automated multi-system correlation
 👨‍🎓 Academic Use

This project is developed for **Final Year Digital Forensics / Cybersecurity** academic submission and viva examination.

 📜 License
This project is intended for **educational purposes only**.
