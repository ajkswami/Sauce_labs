import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
BaseUrl = "https://www.saucedemo.com/"
user_name_locator = "#user-name"
pass_word_locator = "#password"
login_button_locator = "//input[@type='submit']"
msg_locator = "h3"  # Update to the correct locator for the error message

driver.get(BaseUrl)
driver.find_element(By.CSS_SELECTOR, user_name_locator).send_keys("test")
driver.find_element(By.CSS_SELECTOR, pass_word_locator).send_keys("test")
time.sleep(2)
driver.find_element(By.XPATH, login_button_locator).click()
time.sleep(2)

wait = WebDriverWait(driver, 10)
error_msg_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, msg_locator)))

# Get the text of the error message element
txt = error_msg_element.text

print(txt)
