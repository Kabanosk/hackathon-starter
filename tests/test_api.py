import requests


class TestAPI:
    BASE_URL = "http://0.0.0.0:8000"

    def test_main(self):
        response = requests.get(f"{self.BASE_URL}/")
        assert response.status_code == 200

    def test_users(self):
        response = requests.get(f"{self.BASE_URL}/users/1")
        assert response.status_code == 200
