from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the ChromeDriver executable
chrome_driver_path = "C:\\chromedrivers\\chromedriver.exe"

# Create ChromeOptions object and set the executable path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"executable_path={chrome_driver_path}")

# Use ChromeOptions when creating the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://d2vj56vj2lgai5.cloudfront.net")
driver.maximize_window()
print(driver.title)

# Login page 

# Find the input field using the formcontrolname attribute
email_input = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="email"]')
password_input = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="password"]')
login_button = driver.find_element(By.XPATH, "//button(contains, text())").click()

# Send keys to the input field
email_input.send_keys("nitesh@yopmail.com")
password_input.send_keys("Ats@1234")
login_button.click()
driver.close()

# def addition():
#     print(12+34)

# addition()