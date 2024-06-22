import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
element = driver.find_element(By.NAME,"search")
element.click()
element.send_keys("Iphone 15 pro")
time.sleep(2)
element.clear()
time.sleep(2)
element.send_keys("macbook")
time.sleep(2)