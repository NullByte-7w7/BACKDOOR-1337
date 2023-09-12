# SHELL PERSISTENT

![Image](https://github.com/DARKSECshell/shell_persistent/assets/121623691/93b2f403-b4f3-452f-9ca9-ac996a620ecd)

**Disclaimer: This tool is intended for educational and ethical purposes only. The use of this script for any malicious activity is strictly prohibited.**

## Introduction

The **Shell Persistent** tool is designed to help you understand and enhance the security of your own systems or networks. It provides a controlled environment to test and analyze vulnerabilities, allowing you to strengthen your defenses.

## Features

- Gain access to a target machine after they run the script (as the root user).
- Create a shell spawn in the `/tmp` directory to escalate privileges.
- Maintain a persistent shell connection with the victim's machine.
- Compatible with Debian-based systems.

## Warning

**Please use this tool responsibly and only on systems you have explicit permission to test. Unauthorized access or any malicious activities are illegal and unethical.**

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/DARKSECshell/shell_persistent.git
Modify the IP address in the source code to your own IP.

Run the script as the root user on your target machine:
   
   ```bash
 sudo ./shell_persistent.sh
```
Ransomware Alert

This script contains a ransomware component with a payload that encrypts the target's crontab. This is for educational purposes only to demonstrate potential vulnerabilities. Do not use this ransomware component for any malicious activities.

Legal Disclaimer

Use this tool responsibly and in compliance with all applicable laws and regulations. Unauthorized use, distribution, or modification of this tool for malicious purposes is strictly prohibited. The author and contributors of this tool are not responsible for any misuse or illegal activities conducted with it.

Contributing

Feel free to contribute to this project by submitting issues or pull requests. Please ensure your contributions align with ethical coding practices.
