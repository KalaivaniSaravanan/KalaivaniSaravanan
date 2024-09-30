from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Scenario: Ensure new users can register
# and existing users cannot register with the same email.

driver = webdriver.Chrome()
driver.get("https://paywize.com/register")

# Test registration with a new email
driver.find_element(By.ID, "email").send_keys("newuser@example.com")
driver.find_element(By.ID, "password").send_keys("Password123", Keys.RETURN)
confirmation_message = driver.find_element(By.CLASS_NAME, "confirmation").text
assert "Registration successful" in confirmation_message

# Test registration with an existing email
driver.get("https://paywize.com/register")
driver.find_element(By.ID, "email").send_keys("existinguser@example.com")
driver.find_element(By.ID, "password").send_keys("Password123", Keys.RETURN)
error_message = driver.find_element(By.CLASS_NAME, "error").text
assert "Email already in use" in error_message

driver.quit()
