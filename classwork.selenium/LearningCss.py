import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
#driver.find_element(By.CSS_SELECTOR,".btn.btn-default.btn-lg").click()
driver.find_element(By.CSS_SELECTOR,"input[name ='search']").click()
time.sleep(5)
