# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome driver with the path to the ChromeDriver executable
PATH = r"D:\chromedriver-win64\chromedriver.exe"
service = Service(PATH)



# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver = webdriver.Chrome(service=service)

# Set implicit wait time
driver.implicitly_wait(5)

# Maximize the browser window
driver.maximize_window()


# Open the URL
driver.get("https://bing.com")

# Find the search box using name attribute
search_box = driver.find_element("name", "q")
search_box.send_keys("Guru Mohanji")
search_box.send_keys(Keys.RETURN)  # Simulate pressing the Enter key

# Wait for 10 seconds
time.sleep(5)

# Close the browser
driver.quit()

print("Test Successfully Completed")