from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open the SauceDemo website
driver.get("https://www.saucedemo.com/")
time.sleep(3)

# Locate username web element using relative XPath
username = driver.find_element(By.XPATH, "//input[@id='user-name']")
username.send_keys("standard_user")

# Locate password web element using relative XPath
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys("secret_sauce")

time.sleep(2)

# Locate and click the login button
loginBtn = driver.find_element(By.XPATH, "//input[@id='login-button']")
loginBtn.click()

# Wait a few seconds to see the result (optional)
time.sleep(5)

#contains() - locate add to cart button
addToCart = driver.find_element(By.XPATH,"//button[contains(@id,'sauce-labs-bolt-t-shirt')]")
addToCart.click()


#text() - locate web element sauce lab fleece jacket and perform click action
product= driver.find_element(By.XPATH,"//div[text()='Sauce Labs Fleece Jacket']")
product.click()

time.sleep(5)
# Close the browser
driver.quit()
