# One location to another location called locators
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
#driver.find_element(By.NAME,"search").click()
#driver.find_element(By.ID,"cart-total").click()
#driver.find_element(By.LINK_TEXT,"About Us").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"About").click()
time.sleep(5)