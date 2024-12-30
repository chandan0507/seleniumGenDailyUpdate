import time
from postApiCall import apiCall
from selenium import webdriver
from selenium.webdriver.common.by import By

productName = 'vocus'

driver = webdriver.Chrome()
driver.get('https://')
time.sleep(3)
