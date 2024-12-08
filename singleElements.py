# singleElements = ['id', 'name', 'xpath', 'linktext', 'tagname', 'classname', 'cssselector', 'q']
# operationAvail = ['click', 'input']

availSingleElementsDict = {'id': 'ID', 'name': 'NAME', 'xpath': 'XPATH', 'linktext': 'LINK_TEXT', 'tagname': 'TAG_NAME', 'classname': 'CLASS_NAME', 'cssselector': 'CSS_SELECTOR'}
availOperationDict = {'click': 'click', 'input': 'send_keys'}

def getSingleElement(fileName):
    while True:
        # Below will take the parameter from user and converts to lower case
        userInputElement = input(f" Select anyone of the below to get html element & press 'q' to quit: \n {availSingleElementsDict.keys()} : ").lower()
        # Validates if the given user element is present in array of not
        if userInputElement not in availSingleElementsDict.keys():
            continue
        else:
            # if user presses q the program will be existed
            if userInputElement == 'q':
                print('You have existed from the program')
                quit()
            print(f"You have selected : {userInputElement} selector")
            break

#========================================================================

    # Get the value of the element from the user
    while True:
        userInputElementValue = input(f"Please enter value for the element : ")
        if not userInputElementValue:
            continue
        else:
            print(f"You have selected {userInputElementValue}")
            break        

#===========================================================================

    while True:
        # Below will get the opeartion from user and converts to lower case
        userInputOperation = input(f"Please select a opeartion to be performed : {availOperationDict.keys()} : ").lower()
        # checks if the opeartion is avail in array of not
        if userInputOperation not in availOperationDict.keys():
            continue
        else:
            break
    
#================================================================

    while True:
        print(f"You have selected : {userInputOperation} operation")
        if userInputOperation == 'input':
            userInputOperationValue =  input(f"Please enter the opeartion value : ")
            if not userInputOperationValue:
                continue
            else:
                matchCheck(fileName, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue)
                break
        else:
            userInputOperationValue = ""
            matchCheck(fileName, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue)
            break
    quit()

# End of getSingleElement function

def writeElementOperation(fileName, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue):
    f = open(fileName, 'a')
    try:
        f.write(f"content = driver.find_element(By.{userInputElement}, '{userInputElementValue}')\n")
        f.write(f"content.{userInputOperation}('{userInputOperationValue}')\n")
        f.write(f"time.sleep(10)\n")
        f.write("driver.quit()\n")
        f.write("quit()\n")
    except FileNotFoundError:
        print("file not found")

# ==================================

# def writeOpeartion(fileName, userInputOperation, userInputOperationValue):
#     f = open(fileName, 'a')
#     try:
#         f.write(f"content.{userInputOperation}({userInputOperationValue})\n")
#         f.write(f"time.sleep(10)\n")
#         f.write("driver.quit()\n")
#         f.write("quit()\n")
#     except FileNotFoundError:
#         print("file not found")

#=======================================

def matchCheck(fileName, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue=None):
    match userInputElement:
        case 'id':
            writeElementOperation(fileName, availSingleElementsDict['id'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'name':
            writeElementOperation(fileName, availSingleElementsDict['name'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'xpath':
            writeElementOperation(fileName, availSingleElementsDict['xpath'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'linktext':
            writeElementOperation(fileName, availSingleElementsDict['linktext'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'linktext':
            writeElementOperation(fileName, availSingleElementsDict['linktext'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'tagname':
            writeElementOperation(fileName, availSingleElementsDict['tagname'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'classname':
            writeElementOperation(fileName, availSingleElementsDict['classname'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'cssselector':
            writeElementOperation(fileName, availSingleElementsDict['cssselector'], userInputElementValue, userInputOperation, userInputOperationValue)