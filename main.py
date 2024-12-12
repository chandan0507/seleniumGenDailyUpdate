from userInputReceiver import checkDictValidator, checkValueValidator
from urlAndTimer import getUrlFromUser
from matchChecker import matchCheck
from userInputWriter import availOperationDict, availSingleElementsDict

while True:
    fileName = input("Please enter the filename length should be between 5 to 50: ")
    fileName.strip()
    fileNamepy = fileName+".py"
    # instead of none, not is used to check empty or not
    if not fileName:
        continue 
    print(f"Given fileName is {fileNamepy}")
    getUrlFromUser(fileNamepy)
    break

count = 0
while True:
    incrementCounterOnEachCall = "element"
    incrementCounterOnEachCall = incrementCounterOnEachCall+str(count)
    keySelector = checkDictValidator(fileNamepy, "Select anyone of the below to get html element & press 'q' to quit : ", availSingleElementsDict)
    valueSelector = checkValueValidator("Please enter value for the selector : ")
    keyOperator = checkDictValidator(fileNamepy, "Select anyone of the below to get html element & press 'q' to quit : ", availOperationDict)
    valueOperator = ""
    if keyOperator == 'input':
        valueOperator = checkValueValidator("Please enter value for the selector : ")
    description = checkValueValidator("Please provide a specific description for the block : ")
    matchCheck(fileNamepy, incrementCounterOnEachCall, description, keySelector, valueSelector, keyOperator, valueOperator)
    count+=1