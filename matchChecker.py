from userInputWriter import writeElementOperation, availSingleElementsDict

def matchCheck(fileName, incrementCounterOnEachCall, userInputDescription, userInputElement, userInputElementValue, userInputOperation, userInputOperationValue):
    match userInputElement:
        case 'id':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['id'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'name':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['name'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'xpath':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['xpath'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'linktext':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['linktext'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'tagname':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['tagname'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'classname':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['classname'], userInputElementValue, userInputOperation, userInputOperationValue)
        case 'cssselector':
            writeElementOperation(fileName, incrementCounterOnEachCall, userInputDescription, availSingleElementsDict['cssselector'], userInputElementValue, userInputOperation, userInputOperationValue)