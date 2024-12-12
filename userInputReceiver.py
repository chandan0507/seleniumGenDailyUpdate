def checkDictValidator(fileName, definition, dictname):
    while True:
        captureElement = input(f"{definition} \n{dictname.keys()} : ").lower()
        # Validates if the given user element is present in array of not
        if captureElement not in dictname.keys():
            continue
        else:
            # if user presses q the program will be existed
            if captureElement == 'q' and 'q' in dictname.keys():
                print('You have existed from the program')
                f = open(fileName, 'a')
                f.write(f"result = 'PASS'\n")
                f.write(f"captureResponse = apiCall('{fileName}', productName, result)\n")
                f.write(f"print(captureResponse[0].text.strip(), \'testRunId :\', captureResponse[1], \'resultCode :\', captureResponse[0].status_code)\n")
                f.write("driver.quit()\n")
                quit()
            print(f"You have selected : {captureElement}")
            return captureElement
    
def checkValueValidator(definition):
    while True:
        captureValue = input(f"{definition}")
        if not captureValue:
            continue
        else:
            print(f"You have selected : {captureValue}")
            return captureValue
