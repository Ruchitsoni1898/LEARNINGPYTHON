import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
driver.switch_to.new_window("tab")
driver.get("https://www.amazon.de/-/en/")
time.sleep(5)
