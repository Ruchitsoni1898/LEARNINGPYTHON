import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
driver.find_element(By.XPATH,"//input[@name = 'search']").click()
#driver.find_element(By.XPATH,"/html/body/header/div/div/div[2]/div/input").click()
time.sleep(5)