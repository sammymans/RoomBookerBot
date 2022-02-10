from msilib.schema import ServiceControl
import time
from tkinter import E
from webbrowser import Chrome

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from login import user, password
# from selection import room_number, times_requested

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

PATH = "C:\Program Files (x86)\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(PATH)

my_url = "https://learn.ivey.ca/accounts/1/external_tools/532?launch_type=global_navigation"

driver.get(my_url)
driver.maximize_window()

try:
    # outlook ivey login - user(email) and pass
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "userNameInput")))
    element.clear()
    element.send_keys(user)
    print("Username")

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "passwordInput")))
    element.clear()
    element.send_keys(password)
    print("Password")

    # Click Sign In
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    element.click()
    print("Login")

    # We are now at the room booking page, book specific slots now
    # Click Next Day 7 times
    
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/button')))
        print("page is ready")
        element.click()
        print("Next Day")
    except:
        print("took too long / could not find")
    
    print("after")
    

    


except:
    driver.quit()

