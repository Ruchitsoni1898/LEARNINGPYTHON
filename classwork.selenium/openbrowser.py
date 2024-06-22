from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window() #full screen window
driver.get("https://tutorialsninja.com/demo/") # Get the website url
driver.quit() # Closed all the tabs on web browser
#driver.close() - closed the current tab on the browser immediately