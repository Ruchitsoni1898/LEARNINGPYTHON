import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/")
time.sleep(7)
#driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.NAME,"username")))
driver.find_element(By.NAME,"username").click()
