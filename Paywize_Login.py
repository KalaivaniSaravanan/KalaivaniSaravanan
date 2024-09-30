from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Scenario: Verify that users can log in with valid credentials
# and are denied access with invalid credentials.

driver = webdriver.Chrome()
driver.get("https://paywize.com/login")

# Test valid login
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_password", Keys.RETURN)
assert "Dashboard" in driver.title

# Test invalid login
driver.get("https://paywize.com/login")
driver.find_element(By.ID, "username").send_keys("invalid_user")
driver.find_element(By.ID, "password").send_keys("invalid_password", Keys.RETURN)
error_message = driver.find_element(By.CLASS_NAME, "error").text
assert "Invalid credentials" in error_message

driver.quit()
