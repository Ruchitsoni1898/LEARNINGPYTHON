import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")
element = driver.find_element(By.LINK_TEXT,"Desktops")
action = ActionChains(driver)
action.move_to_element(element).perform()
time.sleep(5)