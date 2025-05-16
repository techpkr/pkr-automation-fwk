import pytest
import requests

class APIClient:
    def __init__(self, base_url: str, token: str = ""):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = token

    @property
    def headers(self):
        return {
            "Authorization": f"Bearer {self.token}" if self.token else "",
            "Content-Type": "application/json"
        }

    def get(self, path: str, **kwargs):
        return self.session.get(f"{self.base_url}{path}", headers=self.headers, **kwargs)

    def post(self, path: str, json=None, **kwargs):
        return self.session.post(f"{self.base_url}{path}", headers=self.headers, json=json, **kwargs)

    def close(self):
        self.session.close()


@pytest.fixture(scope="session")
def api_client():
    client = APIClient(base_url="https://<Domain>.com")
    yield client
    client.close()
