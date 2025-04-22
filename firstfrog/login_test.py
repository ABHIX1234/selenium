from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open the SauceDemo website
driver.get("https://www.saucedemo.com/")
time.sleep(3)  # Wait for 3 seconds to ensure the page loads

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


# Validate successful login by checking the presence of a product
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Wait until the product "Sauce Labs Backpack" is visible on the page
    product_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='Sauce Labs Backpack']"))
    )
    print("Login successful. Product found:", product_element.text)
except Exception as e:
    print("Login failed or product not found:", str(e))
#real test new project

# Close the browser
driver.quit()
