import requests
from requests.auth import HTTPBasicAuth
import os

TESTRAIL_URL = os.getenv("TESTRAIL_URL")
TESTRAIL_USER = os.getenv("TESTRAIL_USER")
TESTRAIL_API_KEY = os.getenv("TESTRAIL_API_KEY")
PROJECT_ID = os.getenv("TESTRAIL_PROJECT_ID")
RUN_ID = os.getenv("TESTRAIL_RUN_ID")  # Existing test run id or create one dynamically

def add_result_for_case(case_id: int, status_id: int, comment: str = ""):
    """
    Add test result for a specific case in a test run.
    status_id: 1=Passed, 5=Failed, 3=Skipped etc.
    """
    if not all([TESTRAIL_URL, TESTRAIL_USER, TESTRAIL_API_KEY, RUN_ID]):
        print("TestRail credentials or run ID missing, skipping update")
        return

    url = f"{TESTRAIL_URL}/index.php?/api/v2/add_result_for_case/{RUN_ID}/{case_id}"
    data = {"status_id": status_id, "comment": comment}
    response = requests.post(url, json=data, auth=HTTPBasicAuth(TESTRAIL_USER, TESTRAIL_API_KEY))
    if response.status_code != 200:
        print(f"Failed to update TestRail: {response.status_code} - {response.text}")
