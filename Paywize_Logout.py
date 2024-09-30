driver = webdriver.Chrome()
driver.get("https://paywize.com/login")
# Log in code here...

driver.find_element(By.ID, "logout").click()
assert "Login" in driver.title  # Check if redirected to login page

driver.quit()
