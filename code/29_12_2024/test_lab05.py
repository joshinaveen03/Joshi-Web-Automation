from selenium import webdriver
import time
def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://google.com")

    #driver.navigate()  to x
    print(driver.title)

    #Navigation Command
    driver.back()
    driver.get("https://google.com")
    print(driver.title)

    driver.forward()
    print(driver.title)

    driver.back()
    print(driver.title)
    driver.refresh()

    time.sleep(5)
    driver.quit()