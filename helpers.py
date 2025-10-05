import requests

class TestUser:
    def create_test_user_via_API(self):
        body = {
            "email": "Diplomtest@mail.com",
            "password": "password123",
            "name": "Diplomtest"
            }
        response_create = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', json = body)
        response_login = requests.post(' https://stellarburgers.nomoreparties.site/api/auth/register',json = body)
        