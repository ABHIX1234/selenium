from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Initialize the Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open the SauceDemo website
driver.get("https://www.saucedemo.com/")
time.sleep(5)

# Locate the username field and enter the username
#username = driver.find_element(By.ID, value="user-name")
username = driver.find_element(By.NAME, value="user-name")
username.send_keys("standard_user")

# ✅ Corrected the ID from "passward" to "password"
password = driver.find_element(By.ID, value="password")
password.send_keys("secret_sauce")

time.sleep(5)

# Close the browser
driver.quit()
