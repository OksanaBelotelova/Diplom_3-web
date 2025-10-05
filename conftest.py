import pytest
import requests
from selenium import webdriver
from data import URLs, AuthCredentials


# @pytest.mark.parametrize('web', [webdriver.Chrome, webdriver.Firefox])
@pytest.fixture
def driver():
    url = URLs.test_url
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def create_and_login_user_via_API():
    auth_credentials = AuthCredentials()
    register_response = requests.post(
        'https://stellarburgers.nomoreparties.site/api/auth/register', json=auth_credentials.registration).json()

    yield

    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user',
                    headers={'Authorization': f'{register_response['accessToken']}'})
