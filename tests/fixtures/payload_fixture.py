import pytest
from utils.helpers import load_json_data




@pytest.fixture
def sample_payload():
    return {
        "name": "Prashanth K R",
        "email": "kodurprashanth@gmail.com",
        "username": "pkr"
    }


@pytest.fixture(scope="session")
def user_list():
    return load_json_data("users.json")