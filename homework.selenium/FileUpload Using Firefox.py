import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://pinetools.com/split-image")
driver.find_element(By.NAME,"image").send_keys("E:\\My photos\\unnamed.jpg")
time.sleep(5)
