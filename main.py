import requests
from requests.auth import HTTPBasicAuth
from .env import username, password
import time

basic = HTTPBasicAuth(username=username, password=password)
s = requests.Session()
url = "https://[YOUR_SITE_NAME].legalserver.org/modules/reports/api_export.php?load=[YOUR_REPORTS_API_KEY_HERE]"
headers = {
    "Accept": "application/json, application/xml"
}
response = requests.get(url=url, headers=headers, auth=basic)
status_code = response.status_code
data = response.json()
cases_to_close = []

for json_record in data["data"]:
    cases_to_close.append(json_record["Globally_Unique_ID"])

def bulk_close_cases(cases_to_close: list):
    for case_id in cases_to_close:
        update_url = f"https://[YOUR_SITE_NAME].legalserver.org/api/v2/matters/{case_id}"
        payload = {
            "case_disposition": "Closed"
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/html"
        }
        try:
            session_response = s.patch(url=update_url, headers=headers, data=payload, auth=basic)
            print(f"Updating {case_id} - Status: {session_response.status_code}")
            if status_code != 200:
                print(f"Failed to update {case_id}: {status_code} - {session_response.text}")
            time.sleep(0.35)
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {case_id}: {e}")
            continue
    print("Done with the requests. No more cases to update!")

bulk_close_cases(cases_to_close)