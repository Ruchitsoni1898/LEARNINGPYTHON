import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.LINK_TEXT,"About Us"))
time.sleep(5)