import time

from selenium import webdriver

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.de/-/en/")
time.sleep(5)