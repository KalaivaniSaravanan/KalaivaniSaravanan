from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Scenario: Test that users can successfully complete a payment transaction.

driver = webdriver.Chrome()
driver.get("https://paywize.com/payment")

driver.find_element(By.ID, "amount").send_keys("100")
driver.find_element(By.ID, "payment_method").select_by_visible_text("Credit Card")
driver.find_element(By.ID, "card_number").send_keys("4111111111111111")
driver.find_element(By.ID, "expiration_date").send_keys("12/24")
driver.find_element(By.ID, "cvv").send_keys("123", Keys.RETURN)

success_message = driver.find_element(By.CLASS_NAME, "success").text
assert "Payment successful" in success_message

driver.quit()
