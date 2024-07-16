import requests

# check if subdomain exists
def check_subdomain(company, service, tld):
    url = f"https://{company}.{service}.{tld}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200 and ("login" in response.text.lower() or "sign in" in response.text.lower()):
            return True
    except requests.RequestException:
        pass
    return False

# search for third party portals
def check_company(company):
    services = [
        ("slack", "com"),
        ("monday", "com"),
        ("atlassian", "net"),
        ("zendesk", "com"),
        ("salesforce", "com"),
        ("okta", "com"),
    ]

    found = False
    for service, tld in services:
        if check_subdomain(company, service, tld):
            print(f"Found login portal: {company}.{service}.{tld}")
            found = True

    if not found:
        print(f"No login portals found for {company}")

def main():
    companies = input("Enter company names (comma-separated) that may be included in url: ").split(',')
    companies = [company.strip() for company in companies]

    for company in companies:
        print(f"\nChecking for {company}:")
        check_company(company)

if __name__ == "__main__":
    main()