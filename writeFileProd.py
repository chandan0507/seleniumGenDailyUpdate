def writeProdUrl(fileName, getProductName, urlGet):
    f = open(fileName, "a")
    try:
        f.write("import time\n")
        f.write("from postApiCall import apiCall\n")
        f.write("from selenium import webdriver\n")
        f.write("from selenium.webdriver.common.by import By\n\n")
        f.write(f"productName = '{getProductName}'\n\n")
        f.write("driver = webdriver.Chrome()\n")
        f.write(f"driver.get('{urlGet}')\n")
        f.write(f"time.sleep(3)\n")
    except FileNotFoundError:
        print("file not found")
        f.close()

def checkDictWriter(fileName, selectorKey, dictname):
    while True:
        captureElement = selectorKey.lower()
        # Validates if the given user element is present in array of not
        if captureElement not in dictname.keys():
            break
        else:
            # if user presses q the program will be existed
            return captureElement
        
def checkValueWriter(definition):
    while True:
        captureValue = input(f"{definition}")
        if not captureValue:
            continue
        else:
            print(f"You have selected : {captureValue}")
            return captureValue
