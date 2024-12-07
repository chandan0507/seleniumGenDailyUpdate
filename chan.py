import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://10.0.6.20:8443/tssgui/')
time.sleep(10)
content = driver.find_element(By.ID, 'details-button')
content.click()
time.sleep(10)
driver.quit()
quit()
