# thirdpartyhardy
## SaaS Login Portal Finder

### Description
This Python script is designed to identify potential login portals for various Software as a Service (SaaS) platforms associated with a given company name. It checks common SaaS services by constructing URLs based on the company name and verifying if a login page exists.

### Disclaimer
This tool is for educational and authorized testing purposes only. Always obtain explicit permission before scanning or testing any systems you do not own. Unauthorized use of this script may be illegal and unethical.

### Features
- Accepts multiple company names as input
- Checks for login portals across various popular SaaS platforms
- Basic error handling for network requests

## Installation
1. Clone this repository 
2. Create venv `python3 -m venv venv`
3. Activate venv `source venv/bin/activate`
4. Install requirements.txt `pip install -r requirements.txt`
5. Run (you will be promped to input possible company names (comma separated)): `python3 thirdpartyhardy.py` 
