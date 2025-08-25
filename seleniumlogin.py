import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

username = "standard_user"
password = "secret_sauce"

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.find_element("id", "user-name").send_keys(username)
driver.find_element("id", "password").send_keys(password)
driver.find_element("id", "login-button").click()

