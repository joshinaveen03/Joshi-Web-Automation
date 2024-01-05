import time
from selenium import webdriver
import pytest

def test_open_login():
    chrome_options =webdriver.Chrome()

    driver=webdriver.Chrome()
    driver.get("https://google.com")

    print(driver.title)
    time.sleep(500)