import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=product/category&path=20_27")
dropdown = Select(driver.find_element(By.ID,"input-sort"))
#dropdown.select_by_value("https://tutorialsninja.com/demo/index.php?route=product/category&path=20_27&sort=p.price&order=ASC&limit=50")
dropdown.select_by_visible_text("Price (High > Low)")
time.sleep(5)
