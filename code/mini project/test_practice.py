import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.test.case
def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # Verifying Test Case
    print(driver.current_url)
    assert driver.current_url=="https://app.vwo.com/#/login"

    #element:#class ="text-input W(100%)" name="username"
    # id="login-username" data-qa="hocewoqisi" >

    username=driver.find_element(By.NAME,"username" )
    username.send_keys("contact+atb5x@thetestingacademy.com")

    #element <input type="password" class="text-input W(100%)" name="password"
    # id="login-password" data-qa="jobodapuxe">

    password=driver.find_element(By.NAME,"password")
    password.send_keys("ATBx@1234")

    #element <button type="submit" id="js-login-btn" class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)" data-qa="sibequkica"><span class="icon loader hidden"
    # data-qa="zuyezasugu"></span><span data-qa="ezazsuguuy">Sign in</span></button>

    on_submit=driver.find_element(By.ID,"js-login-btn")
    on_submit.click()

    time.sleep(10)
    driver.quit()