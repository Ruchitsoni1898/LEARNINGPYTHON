import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.maximize_window()
driver.get("https://www.amazon.de/-/en/")
element = driver.find_element(By.NAME,"field-keywords")
element.click()
element.send_keys("HP victus")
time.sleep(5)
element.clear()
time.sleep(2)
element.send_keys("LCD TV")
time.sleep(2)