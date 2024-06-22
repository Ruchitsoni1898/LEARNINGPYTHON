import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
driver.refresh()
driver.get("https://www.amazon.de/-/en/")
driver.back()
time.sleep(3)
driver.forward()