# thirdpartyhardy
## SaaS Login Portal Finder

### Description
Python script designed to identify potential login portals for various Software as a Service (SaaS) platforms associated with a given company name. It checks common SaaS services (monday,slack,okta,atlassian,zendesk,salesforce) by constructing URLs based on the company name and verifying if a login page exists.

### partyyyyyyyhardyyyyyy
- Accepts multiple company names as input
- Checks for login portals across various popular SaaS platforms
- Basic error handling for network requests

## Installation
1. Clone this repository 
2. Create venv `python3 -m venv venv`
3. Activate venv `source venv/bin/activate`
4. Install requirements.txt `pip install -r requirements.txt`
5. Run (you will be promped to input possible company names (comma separated)): `python3 thirdpartyhardy.py` 
