### Domain Recon Tool
### Overview
The Domain Recon Tool is a Python-based reconnaissance tool designed to gather WHOIS information and DNS records of a given domain. It provides a simple and interactive GUI for users to perform domain reconnaissance efficiently.

Features
WHOIS Lookup
DNS Enumeration (A, AAAA, MX, NS, TXT, SOA)
GUI with a futuristic theme
Copy results to clipboard
Save logs automatically
Installation
Prerequisites
Ensure you have Python 3 installed. If not, install it from Python.org.

Install Required Modules
Create a virtual environment (recommended) and install dependencies:

bash
Copy
Edit
python3 -m venv venv  
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`  
pip install -r requirements.txt  
If using Kali Linux, install dependencies manually:

bash
Copy
Edit
sudo apt install python3-tk python3-dnspython python3-whois  
Usage
Run the tool using:

bash
Copy
Edit
python3 domain_recon.py  
Enter the target domain in the input field.
Click Start Scan to begin reconnaissance.
View results in the output section.
Use Copy Results to copy findings to the clipboard.
Requirements
The dependencies are listed in requirements.txt:

perl
Copy
Edit
whois
dnspython
requests
socket
tk
Screenshots
(Add screenshots of the GUI here if available)

License
This project is open-source and available under the MIT License.


