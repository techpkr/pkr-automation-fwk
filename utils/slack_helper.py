import requests
import os

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_message(message: str):
    if not SLACK_WEBHOOK_URL:
        print("Slack webhook URL not set, skipping notification")
        return
    
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        print(f"Failed to send Slack message: {response.status_code}, {response.text}")
