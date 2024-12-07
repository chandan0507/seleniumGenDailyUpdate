# singleElements = ['id', 'name', 'xpath', 'linktext', 'tagname', 'classname', 'cssselector', 'q']
# operationAvail = ['click', 'input']

singleElementsDict = {'id': 'ID', 'name': 'NAME', 'xpath': 'XPATH', 'linktext': 'LINK_TEXT', 'tagname': 'TAG_NAME', 'classname': 'CLASS_NAME', 'cssselector': 'CSS_SELECTOR'}
operationAvailDict = {'click': 'click', 'input': 'send_keys'}

def getSingleElement(fileName):
    while True:
        # Below will take the parameter from user and converts to lower case
        userSelectedElement = input(f" Select anyone of the below to get html element & press 'q' to quit: \n {singleElementsDict.keys()} \n").lower()
        # Validates if the given user element is present in array of not
        if userSelectedElement not in singleElementsDict.keys():
            continue
        else:
            # if user presses q the program will be existed
            if userSelectedElement == 'q':
                print('You have existed from the program')
                quit()
            print(f"You have selected : {userSelectedElement} selector\n")
            break

#========================================================================

    # Get the value of the element from the user
    while True:
        elementValue = input(f"Please enter value for the element\n")
        if not elementValue:
            continue
        else:
            print(f"You have selected {elementValue}")
            break        

#===========================================================================

    while True:
        # Below will get the opeartion from user and converts to lower case
        operationUserInput = input(f"Please select a opeartion to be performed : {operationAvailDict.keys()}\n").lower()
        # checks if the opeartion is avail in array of not
        if operationUserInput not in operationAvailDict.keys():
            continue
        else:
            print(f"You have selected : {operationUserInput} operation\n")
            break
    
#================================================================

    while True:
        if operationUserInput is 'input':
            userOperationVal =  input(f"Please enter the opeartion value : \n")
            if not userOperationVal:
                continue
            else:
                break
        else:
            userOperationVal = ""
            matchCheck(userSelectedElement, fileName, elementValue, operationUserInput, userOperationVal)
            break
    quit()

# End of getSingleElement function

def writeElement(fileName, selector, elementVal):
    f = open(fileName, 'a')
    try:
        f.write(f"content = driver.find_element(By.{selector}, '{elementVal}')\n")
        # f.write("driver.quit()\n")
        # f.write("quit()\n")
    except FileNotFoundError:
        print("file not found")

# ==================================

def writeOpeartion(fileName, operation, operationWithinVal):
    f = open(fileName, 'a')
    try:
        f.write(f"content.{operation}({operationWithinVal})\n")
        f.write(f"time.sleep(10)\n")
        f.write("driver.quit()\n")
        f.write("quit()\n")
    except FileNotFoundError:
        print("file not found")

#=======================================

def matchCheck(singleElement, fileName, userElement, userOperation, userOperationVal=None):
    match singleElement:
        case 'id':
            writeElement(fileName, singleElementsDict['id'], userElement)
            writeOpeartion(fileName, userOperation, userOperationVal)
        case 'name':
            writeElement(fileName, singleElementsDict['name'], userElement)
            writeOpeartion(fileName, userOperation, userOperationVal)
        case 'xpath':
            writeElement(fileName, singleElementsDict['xpath'], userElement)
            writeOpeartion(fileName, userOperation, userOperationVal)
        case 'linktext':
            writeElement(fileName, singleElementsDict['linktext'], userElement)
            writeOpeartion(fileName, userOperation, userOperationVal)
        case 'linktext':
            writeElement(fileName, singleElementsDict['linktext'], userElement)
            writeOpeartion(fileName, userOperation, userOperationVal)
        case 'tagname':
            writeElement(fileName, singleElementsDict['tagname'], userElement)
            writeOpeartion(fileName, userOperation, userOperationVal)
        case 'classname':
            writeElement(fileName, singleElementsDict['classname'], userElement)
            writeOpeartion(fileName, userOperation, userOperationVal)
        case 'cssselector':
            writeElement(fileName, singleElementsDict['cssselector'], userElement)
            writeOpeartion(fileName, userOperation, userOperationVal)