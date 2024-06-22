from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

links = driver.find_elements(By.TAG_NAME,"a")
for x in links:

    print(x.text)
    print(x.get_attribute("href"))