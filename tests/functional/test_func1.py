import pytest

class TestResilienceAPI:

    def test_get_users(self, api_client):
        response = api_client.get("/users")
        assert response.status_code == 200

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "user_data",
        [
            {"name": "Prashanth K R", "email": "pkr@example.com", "username": "pkr"},
            {"name": "Prashu", "email": "pkr039@example.com", "username": "pkr039"},
        ]
    )
    def test_create_user(self, api_client, user_data):
        response = api_client.post("/users", json=user_data)
        assert response.status_code in [200, 201]

    @pytest.mark.skip(reason="Skipping the test temporarily")
    def test_skip(self, api_client):
        response = api_client.get("/users/039")
        assert response.status_code == 404
