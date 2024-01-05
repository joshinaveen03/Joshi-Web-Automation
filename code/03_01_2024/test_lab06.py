from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_open_login():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_btn=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_btn.click()

    time.sleep(5)
    print(driver.title)



    #click on make appointment
    #<a
    # id="btn-make-appointment"
    # href="./index.php#appointment"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>

