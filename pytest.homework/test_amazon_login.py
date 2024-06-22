import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def open_website():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.de/-/en/")

@pytest.mark.smoke
def test_amazon_login():
    open_website()
    driver.find_element(By.LINK_TEXT,"Sign in").click()
    print(driver.title)

def test_amazon_login_perform():
    open_website()
    driver.find_element(By.LINK_TEXT,"Sign in").click()
    emailadr = driver.find_element(By.NAME,"email")
    emailadr.click()
    emailadr.send_keys("ruchitsoni1898@gmail.com")