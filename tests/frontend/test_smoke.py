import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

URL = 'https://testqastudio.me'

# @pytest.mark.xfail(reason="Wait for fix bug")
def test_browser(browser):
    """
    Main fixture
    """
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
    element = browser.find_element(by=By.CSS_SELECTOR, value='[class*="post-11340"]')
    element.click()
    sku = browser.find_element(By.CLASS_NAME, value="sku")

    assert sku.text == 'BFB9ZOK210', "Unexpected sku"