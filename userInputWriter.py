from urlAndTimer import getTimer

availSingleElementsDict = {'id': 'ID', 'name': 'NAME', 'xpath': 'XPATH', 'linktext': 'LINK_TEXT', 'tagname': 'TAG_NAME', 'classname': 'CLASS_NAME', 'cssselector': 'CSS_SELECTOR', 'q': 'quit()'}
availOperationDict = {'click': 'click', 'input': 'send_keys'}

def writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue):
    f = open(fileName, 'a')
    # getTimer function is called here, because to give manual sleep on each operation
    waitTime = getTimer()
    incrementCounterOnEachCallError = incrementCounterOnEachCall+"Error"
    try:
        f.write(f"try:\n")
        f.write(f"\t{incrementCounterOnEachCall} = driver.find_element(By.{userInputElement}, '{userInputElementValue}')\n")
        if userInputOperation == 'click':
            f.write(f"\t{incrementCounterOnEachCall}.{userInputOperation}()\n")
            f.write(f"\tprint('Execution : {userInputDescription}')\n")
        else:
            f.write(f"\t{incrementCounterOnEachCall}.{availOperationDict[userInputOperation]}('{userInputOperationValue}')\n")
            f.write(f"\tprint('Execution : {userInputDescription}')\n")
        f.write(f"except Exception as {incrementCounterOnEachCallError}:\n")
        f.write(f"\tprint('Received an exception : ', {incrementCounterOnEachCallError})\n")
        f.write(f"\tresult = 'FAIL'\n")
        f.write(f"\tcaptureResponse = apiCall('{fileName}', productName, result)\n")
        f.write(f"\tprint(captureResponse[0].text.strip(), \'testRunId :\', captureResponse[1], \'resultCode :\', captureResponse[0].status_code)\n")
        f.write(f"\tdriver.quit()\n")
        f.write(f"\tquit()\n")
        f.write(f"time.sleep({waitTime})\n\n")
    except FileNotFoundError:
        print("file not found")