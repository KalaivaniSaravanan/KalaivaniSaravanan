import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestCompanyLogin(unittest.TestCase):

    def setUp(self):
        # Initialize WebDriver (Chrome in this case)
        self.driver = webdriver.Chrome()  # Make sure you have ChromeDriver in your PATH
        self.driver.get("https://hive.zethic.xyz/")  # Open the login page

    def test_valid_login(self):
        driver = self.driver

        # Locate the username field and enter the username
        username_field = driver.find_element(By.ID, "email")
        username_field.send_keys("company@zethic.com")

        # Locate the password field and enter the password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("company@123")

        # Submit the form
        password_field.send_keys(Keys.ENTER)

        # Wait for the page to load
        time.sleep(3)

        # Check if login was successful, based on URL or page title, etc.
        # Adjust the condition according to the actual behavior after a successful login
        self.assertIn("dashboard", driver.current_url)

    def test_invalid_login(self):
        driver = self.driver

        # Locate the username field and enter an invalid username
        username_field = driver.find_element(By.ID, "email")
        username_field.send_keys("invalid@zethic.com")

        # Locate the password field and enter an invalid password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("invalidpassword")

        # Submit the form
        password_field.send_keys(Keys.ENTER)

        # Wait for the page to load
        time.sleep(3)

        # Check for login failure (you might need to find the exact element that shows an error message)
        error_message = driver.find_element(By.CLASS_NAME,
                                            "error-message-class")  # Adjust based on actual error message class
        self.assertIn("Invalid", error_message.text)

    def tearDown(self):
        # Close the browser after test
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
