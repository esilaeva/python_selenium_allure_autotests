import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

URL = 'https://testqastudio.me'

@pytest.fixture(scope='session')
def browser():
    """
    Main fixture
    """

    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url=URL)
    yield driver
    driver.quit()