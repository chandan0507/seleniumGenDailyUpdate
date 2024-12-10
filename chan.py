import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://10.0.6.46:8443/pcc/welcome/jsp/login.jsp')
time.sleep(2)
try:
	element0 = driver.find_element(By.XPATH, '//*[@id="details-button"]')
	element0.click()
	print('Execution : click on advace option')
except Exception as element0Error:
	print('Received an exception : ', element0Error)
	driver.quit()
	quit()
time.sleep(2)

try:
	element1 = driver.find_element(By.XPATH, '//*[@id="proceed-link"]')
	element1.click()
	print('Execution : click on proceed unsafe option')
except Exception as element1Error:
	print('Received an exception : ', element1Error)
	driver.quit()
	quit()
time.sleep(2)

try:
	element2 = driver.find_element(By.ID, 'username')
	element2.send_keys('admin')
	print('Execution : gave input as admin')
except Exception as element2Error:
	print('Received an exception : ', element2Error)
	driver.quit()
	quit()
time.sleep(2)

try:
	element3 = driver.find_element(By.NAME, 'password')
	element3.send_keys('T4y4n4')
	print('Execution : gave password for the username')
except Exception as element3Error:
	print('Received an exception : ', element3Error)
	driver.quit()
	quit()
time.sleep(2)

try:
	element4 = driver.find_element(By.ID, 'subBtn')
	element4.click()
	print('Execution : click on submit button')
except Exception as element4Error:
	print('Received an exception : ', element4Error)
	driver.quit()
	quit()
time.sleep(10)

driver.quit()
