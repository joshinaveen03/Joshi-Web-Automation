from selenium import webdriver

def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    print(driver.title)