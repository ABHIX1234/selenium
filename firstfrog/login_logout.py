from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Repeat login and logout 10 times
for i in range(10):
    print(f"--- Iteration {i+1} ---")

    # Open the SauceDemo website
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Enter username
    username = driver.find_element(By.XPATH, "//input[@id='user-name']")
    username.send_keys("standard_user")

    # Enter password
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("secret_sauce")

    # Click login button
    loginBtn = driver.find_element(By.XPATH, "//input[@id='login-button']")
    loginBtn.click()
    time.sleep(2)

    # Click on the menu (burger) button
    menuBtn = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
    menuBtn.click()
    time.sleep(1)

    # Click the logout link
    logoutBtn = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
    logoutBtn.click()
    time.sleep(2)

# Close the browser after all iterations
driver.quit()
