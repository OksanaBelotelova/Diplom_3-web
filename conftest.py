import pytest
import requests
from selenium import webdriver
from data import URLs, AuthCredentials




@pytest.fixture(params=['chrome','firefox'])
def driver(request):
    url = URLs.test_url
    browser_name = request.param
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True, scope='session')
def create_user_via_API():
    auth_credentials = AuthCredentials()
    register_response = requests.post(
        URLs.create_user_endpoint, json=auth_credentials.registration).json()

    
    yield

    requests.delete(URLs.delete_user_endpoint,
                    headers={'Authorization': f'{register_response['accessToken']}'})



   