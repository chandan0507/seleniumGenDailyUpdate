import time
from postApiCall import apiCall
from selenium import webdriver
from selenium.webdriver.common.by import By

productName = 'vocus'

driver = webdriver.Chrome()
driver.get('https://')
time.sleep(3)
try:
	element0 = driver.find_element(By.ID, 'someButton')
	element0.click()
	print('Execution : click on button')
except Exception as element0Error:
	print('Received an exception : ', element0Error)
	result = 'FAIL'
	captureResponse = apiCall('yoyoBro.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(10)

try:
	element1 = driver.find_element(By.NAME, 'event')
	element1.click()
	print('Execution : click on button')
except Exception as element1Error:
	print('Received an exception : ', element1Error)
	result = 'FAIL'
	captureResponse = apiCall('yoyoBro.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(10)

try:
	element2 = driver.find_element(By.LINK_TEXT, 'aref')
	element2.send_keys('thisVal')
	print('Execution : click on button')
except Exception as element2Error:
	print('Received an exception : ', element2Error)
	result = 'FAIL'
	captureResponse = apiCall('yoyoBro.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(10)

