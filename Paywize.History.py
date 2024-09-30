from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Scenario: Check that users can view their transaction history.

driver = webdriver.Chrome()
driver.get("https://paywize.com/login")
# Log in code here:
driver.find_element(By.ID, "username").send_keys("valid_user")
driver.find_element(By.ID, "password").send_keys("valid_password", Keys.RETURN)
assert "Dashboard" in driver.title

driver.get("https://paywize.com/transactions")
transactions = driver.find_elements(By.CLASS_NAME, "transaction")

assert len(transactions) > 0  # Check if transactions are listed

driver.quit()
