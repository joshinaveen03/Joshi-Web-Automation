from selenium import webdriver
import logging
import pytest

def test_open_login():
    driver=webdriver.Chrome()
    LOGGER = logging.getLogger(__name__)


    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    LOGGER.info(driver.title)
    print("This is Joshi")
