import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    rel_xpath_email=driver.find_element(By.XPATH,"//*[@id='login-username']")
    rel_xpath_email.send_keys("contact+atb5x@thetestingacademy.com")

    rel_xpath_password=driver.find_element(By.XPATH,"//*[@id='login-password']")
    rel_xpath_password.send_keys("ATBx@1234")

    rel_xpath_submit=driver.find_element(By.XPATH,"//*[@id='js-login-btn']")
    rel_xpath_submit.click()

    time.sleep(10)
    driver.quit()

