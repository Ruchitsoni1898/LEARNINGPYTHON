import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def open_website():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

@pytest.mark.smoke
def test_do_login():
    open_website()
    driver.find_element(By.LINK_TEXT,"My Account").click()
    driver.find_element(By.LINK_TEXT,"Login").click()
    print(driver.title)

def test_perform_login():
    open_website()
    driver.find_element(By.LINK_TEXT, "My Account").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    username = driver.find_element(By.NAME,"email")
    username.click()
    username.send_keys("ruchitsoni1898@gmail.com")
    password = driver.find_element(By.NAME,"password")
    password.click()
    password.send_keys("123456")


