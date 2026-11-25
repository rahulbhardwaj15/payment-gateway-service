import requests

def process_payment():
    session = requests.Session()
    # Triggers CVE-2024-35195 on requests < 2.32.0
    response = session.get("https://api.example-bank.com/pay", verify=False)
    return response.status_code
