import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.amazon.de/-/en/")
element = driver.find_element(By.LINK_TEXT,"Gift Cards")
action = ActionChains(driver)
action.move_to_element(element).perform()
time.sleep(5)