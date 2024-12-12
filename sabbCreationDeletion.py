import time
from postApiCall import apiCall
from selenium import webdriver
from selenium.webdriver.common.by import By

productName = 'wicp'

driver = webdriver.Chrome()
driver.get('https://10.0.6.46:8443/pcc/welcome/jsp/login.jsp')
time.sleep(2)
try:
	element0 = driver.find_element(By.XPATH, '//*[@id="details-button"]')
	element0.click()
	print('Execution : click on advace')
except Exception as element0Error:
	print('Received an exception : ', element0Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element1 = driver.find_element(By.LINK_TEXT, 'Proceed to 10.0.6.46 (unsafe)')
	element1.click()
	print('Execution : click on unsafe')
except Exception as element1Error:
	print('Received an exception : ', element1Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element2 = driver.find_element(By.ID, 'username')
	element2.send_keys('admin')
	print('Execution : gave username')
except Exception as element2Error:
	print('Received an exception : ', element2Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element3 = driver.find_element(By.NAME, 'password')
	element3.send_keys('T4y4n4')
	print('Execution : gave password')
except Exception as element3Error:
	print('Received an exception : ', element3Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element4 = driver.find_element(By.ID, 'subBtn')
	element4.click()
	print('Execution : click on submit')
except Exception as element4Error:
	print('Received an exception : ', element4Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element5 = driver.find_element(By.XPATH, '//*[@id="contentDiv"]/section[2]/div[2]/div/div/div[5]/div/div[2]/ul/li[2]/a/b')
	element5.click()
	print('Execution : click on service Attribute option in home page')
except Exception as element5Error:
	print('Received an exception : ', element5Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element6 = driver.find_element(By.XPATH, '//*[@id="tableBtnsConfigDivId"]/div/span[1]/i')
	element6.click()
	print('Execution : click to add new sabb attribute')
except Exception as element6Error:
	print('Received an exception : ', element6Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element7 = driver.find_element(By.ID, 'sabbName')
	element7.send_keys('newChanSabb')
	print('Execution : gave name for sabb')
except Exception as element7Error:
	print('Received an exception : ', element7Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element8 = driver.find_element(By.ID, 'serviceSB')
	element8.click()
	print('Execution : click on service sabb')
except Exception as element8Error:
	print('Received an exception : ', element8Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element9 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/section[2]/div[3]/div/div/form/div/div[1]/div[1]/div[1]/div[2]/select/option[4]')
	element9.click()
	print('Execution : click on origination call')
except Exception as element9Error:
	print('Received an exception : ', element9Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element10 = driver.find_element(By.ID, 'descCfgTA')
	element10.send_keys('any description')
	print('Execution : gave description for sabb')
except Exception as element10Error:
	print('Received an exception : ', element10Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element11 = driver.find_element(By.NAME, 'categorySB_G0_G1_R1')
	element11.click()
	print('Execution : clicked on attribute')
except Exception as element11Error:
	print('Received an exception : ', element11Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element11 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/section[2]/div[3]/div/div/form/div/div[1]/div[1]/div[2]/div[1]/ul/li/div/div/ul/li[2]/div/div[2]/div/div/div[1]/select/option[2]')
	element11.click()
	print('Execution : clicked on attribute')
except Exception as element11Error:
	print('Received an exception : ', element11Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element12 = driver.find_element(By.NAME, 'paramSB_G0_G1_R1')
	element12.click()
	print('Execution : clicked on parameter')
except Exception as element12Error:
	print('Received an exception : ', element12Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element13 = driver.find_element(By.XPATH, '//*[@id="paramSB_G0_G1_R1"]/option[2]')
	element13.click()
	print('Execution : click on calling party address option')
except Exception as element13Error:
	print('Received an exception : ', element13Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element14 = driver.find_element(By.XPATH, '//*[@id="paramOpSB_G0_G1_R1"]')
	element14.click()
	print('Execution : click on mathematical opeartion')
except Exception as element14Error:
	print('Received an exception : ', element14Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element15 = driver.find_element(By.XPATH, '//*[@id="paramOpSB_G0_G1_R1"]/option[2]')
	element15.click()
	print('Execution : clicked on equal option')
except Exception as element15Error:
	print('Received an exception : ', element15Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element16 = driver.find_element(By.ID, 'paramVal_G0_G1_R1')
	element16.send_keys('248909182')
	print('Execution : should change here to input')
except Exception as element16Error:
	print('Received an exception : ', element16Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element17 = driver.find_element(By.ID, 'select2-categoryVal_1-container')
	element17.click()
	print('Execution : click on inner rule')
except Exception as element17Error:
	print('Received an exception : ', element17Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element18 = driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')
	element18.click()
	print('Execution : inner rule as originating call')
except Exception as element18Error:
	print('Received an exception : ', element18Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element19 = driver.find_element(By.ID, 'select2-outputVal_1-container')
	element19.click()
	print('Execution : click on value selection of inner rule')
except Exception as element19Error:
	print('Received an exception : ', element19Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element20 = driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')
	element20.click()
	print('Execution : click on home location')
except Exception as element20Error:
	print('Received an exception : ', element20Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element21 = driver.find_element(By.ID, 'select2-categoryVal-container')
	element21.click()
	print('Execution : click on outter selector')
except Exception as element21Error:
	print('Received an exception : ', element21Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element22 = driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')
	element22.click()
	print('Execution : click to origination call option on outter layer')
except Exception as element22Error:
	print('Received an exception : ', element22Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element23 = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/section[2]/div[3]/div/div/form/div/div[1]/div[1]/div[2]/div[2]/div[2]/span/span[1]/span/span[1]')
	element23.click()
	print('Execution : click on orginating call now for selection')
except Exception as element23Error:
	print('Received an exception : ', element23Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element24 = driver.find_element(By.XPATH, '/html/body/span/span/span[2]/ul/li[3]')
	element24.click()
	print('Execution : click on outter selector value option')
except Exception as element24Error:
	print('Received an exception : ', element24Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element26 = driver.find_element(By.XPATH, '//*[@id="divAddMain"]/div[4]/div[2]/button')
	element26.click()
	print('Execution : click on add sabb option')
except Exception as element26Error:
	print('Received an exception : ', element26Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element27 = driver.find_element(By.XPATH, '/html/body/div[6]/div[7]/div/button')
	element27.click()
	print('Execution : click on yes option for creation')
except Exception as element27Error:
	print('Received an exception : ', element27Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element28 = driver.find_element(By.XPATH, '//*[@id="viewConfigTable_filter"]/label/input')
	element28.send_keys('newChanSabb')
	print('Execution : required sabb is selected')
except Exception as element28Error:
	print('Received an exception : ', element28Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element29 = driver.find_element(By.XPATH, '//*[@id="viewConfigTable"]/tbody/tr/td[6]/i')
	element29.click()
	print('Execution : click on delete icon')
except Exception as element29Error:
	print('Received an exception : ', element29Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(2)

try:
	element30 = driver.find_element(By.XPATH, '/html/body/div[6]/div[7]/div/button')
	element30.click()
	print('Execution : click on delete confirmation option')
except Exception as element30Error:
	print('Received an exception : ', element30Error)
	result = 'FAIL'
	captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
	print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
	driver.quit()
	quit()
time.sleep(10)

result = 'PASS'
captureResponse = apiCall('sabbCreationDeletion.py', productName, result)
print(captureResponse[0].text.strip(), 'testRunId :', captureResponse[1], 'resultCode :', captureResponse[0].status_code)
driver.quit()
