import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.de/-/en/")
#driver.find_element(By.NAME,"field-keywords").click()
#driver.find_element(By.ID,"nav-cart-count").click()
driver.find_element(By.LINK_TEXT,"Best Sellers").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Amazon").click()
time.sleep(5)
