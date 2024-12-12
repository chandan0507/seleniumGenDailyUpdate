def getUrlFromUser(fileName):

    while(True):
        getProductName = input("Please provide the Product Name : ")
        if not getProductName:
            continue
        else:
            break

    # below will be always true
    while(True):
        urlGet = str(input("Please provide the home page url : "))
        if not urlGet:
            continue
        else:
            waitTime = getTimer()
            break

#============================================
    
# From below writing into file starts

    f = open(fileName, "a")
    try:
        f.write("import time\n")
        f.write("from postApiCall import apiCall\n")
        f.write("from selenium import webdriver\n")
        f.write("from selenium.webdriver.common.by import By\n\n")
        f.write(f"productName = '{getProductName}'\n\n")
        f.write("driver = webdriver.Chrome()\n")
        f.write(f"driver.get('{urlGet}')\n")
        f.write(f"time.sleep({waitTime})\n")
        # f.write("driver.quit()\n")
        # f.write("quit()\n")
    except FileNotFoundError:
        print("file not found")
        f.close()

def getTimer():
    while(True):
        try:
            waitTime = int(input("Plese enter sleep time : "))
            if not waitTime:
                continue
            return waitTime
        except ValueError:
            continue
    