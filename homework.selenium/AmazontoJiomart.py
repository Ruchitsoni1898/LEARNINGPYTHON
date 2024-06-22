import time

from selenium import webdriver

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.de/-/en/")
driver.refresh()
driver.get("https://www.jiomart.com/")
driver.back()
time.sleep(5)
driver.forward()