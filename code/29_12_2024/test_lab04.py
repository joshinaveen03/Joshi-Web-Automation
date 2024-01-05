from selenium import webdriver
import time
def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://google.com")
    print(driver.title)

    time.sleep(5)

    #driver.close()# close will close the current window(tab)
    #It will not close the other tabs
    #session !=null(Invalid)

    driver.quit()
    #session==None
    #close all the tabs(windows)


