from getUrl import getTimer

# singleElements = ['id', 'name', 'xpath', 'linktext', 'tagname', 'classname', 'cssselector', 'q']
# operationAvail = ['click', 'input']

availSingleElementsDict = {'id': 'ID', 'name': 'NAME', 'xpath': 'XPATH', 'linktext': 'LINK_TEXT', 'tagname': 'TAG_NAME', 'classname': 'CLASS_NAME', 'cssselector': 'CSS_SELECTOR', 'q': 'quit()'}
availOperationDict = {'click': 'click', 'input': 'send_keys'}

def getSingleElement(fileName, incrementCounterOnEachCall):
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
                f = open(fileName, 'a')
                f.write("driver.quit()\n")
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
                matchCheck(fileName, incrementCounterOnEachCall, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue)
                break
        else:
            userInputOperationValue = None
            matchCheck(fileName, incrementCounterOnEachCall, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue)
            break

# End of getSingleElement function

def writeElementOperation(fileName, incrementCounterOnEachCall, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue):
    f = open(fileName, 'a')
    # getTimer function is called here, because to give manual sleep on each operation
    waitTime = getTimer()
    try:
        f.write(f"{incrementCounterOnEachCall} = driver.find_element(By.{userInputElement}, '{userInputElementValue}')\n")
        if userInputOperation == 'click':
            f.write(f"{incrementCounterOnEachCall}.{userInputOperation}()\n")
        else:
            f.write(f"{incrementCounterOnEachCall}.{availOperationDict[userInputOperation]}('{userInputOperationValue}')\n")
        f.write(f"time.sleep({waitTime})\n")
        # f.write("driver.quit()\n")
    except FileNotFoundError:
        print("file not found")

#=======================================

def matchCheck(fileName, incrementCounterOnEachCall, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue):
    match userInputElement:
        case 'id':
            writeElementOperation(fileName, incrementCounterOnEachCall, availSingleElementsDict['id'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'name':
            writeElementOperation(fileName, incrementCounterOnEachCall, availSingleElementsDict['name'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'xpath':
            writeElementOperation(fileName, incrementCounterOnEachCall, availSingleElementsDict['xpath'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'linktext':
            writeElementOperation(fileName, incrementCounterOnEachCall, availSingleElementsDict['linktext'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'linktext':
            writeElementOperation(fileName, incrementCounterOnEachCall, availSingleElementsDict['linktext'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'tagname':
            writeElementOperation(fileName, incrementCounterOnEachCall, availSingleElementsDict['tagname'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'classname':
            writeElementOperation(fileName, incrementCounterOnEachCall, availSingleElementsDict['classname'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'cssselector':
            writeElementOperation(fileName, incrementCounterOnEachCall, availSingleElementsDict['cssselector'], userInputElementValue, userInputOperation, userInputOperationValue)