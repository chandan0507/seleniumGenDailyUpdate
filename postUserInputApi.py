from flask import jsonify, request
from userInputReceiver import checkDictValidator, checkValueValidator
from urlAndTimer import getUrlFromUser
from matchChecker import matchCheck
from userInputWriter import availOperationDict, availSingleElementsDict

def postUserInput():
    if request.method == 'POST':
        jsonData = request.get_json()
        # Below checks if jsonData['txnId'] has any value or not, if no value then retuns 402 response
        if not jsonData['txnId']:
            return jsonify({'errorMessage' : 'tnxId is null'}), 402
        if not(5<= len(jsonData['fileName']) <=20):
            return jsonify({'errorMessage' : 'fileName length should be between 5 & 20'}), 405
        if not jsonData['webUrl']:
            return jsonify({'errorMessage' : 'webUrl is null'}), 402
        if not jsonData['productName']:
            return jsonify({'errorMessage' : 'productName is null'}), 402
        for action in jsonData['actions']:
            if not action['selectorKey']:
                return jsonify({'errorMessage' : 'selectorKey is null'}), 402
            if not action['selectorValue']:
                return jsonify({'errorMessage' : 'selectorValue is null'}), 402
            if not action['waitTime']:
                return jsonify({'errorMessage' : 'waitTime is null'}), 402
            if not action['optionKey']:
                return jsonify({'errorMessage' : 'optionKey is null'}), 402
            if not action['description']:
                return jsonify({'errorMessage' : 'description is null'}), 402
            if not action['optionValue']:
                pass
        if jsonData:
            print(dict(jsonData))
        return jsonify({'errorMessage' : 'Success'}), 201


def provideResponse(fileName, webUrl, actions):
    fileName = fileName.strip()
    fileNamepy = fileName+".py"
    print(f"Given fileName is {fileNamepy}")
    getUrlFromUser(fileNamepy)
    
# Below is the body for api, request. action is an array so multiple dictionary could be included

# {
#     "txnId" : "9721628",
#     "fileName" : "chand",
#     "webUrl" : "https://",
#     "productName" : "vocus",
#     "actions" : [
#         {
#             "selectorKey" : "Id",
#             "selectorValue" : "someButton",
#             "optionKey" : "something",
#             "optionValue" : "thisVal",
#             "waitTime" : 10,
#             "description" : "click on button"
#         },
#         {
#             "selectorKey" : "name",
#             "selectorValue" : "event",
#             "optionKey" : "something",
#             "optionValue" : null,
#             "waitTime" : 10,
#             "description" : "click on button"
#         },
#         {
#             "selectorKey" : "link",
#             "selectorValue" : "aref",
#             "optionKey" : "something",
#             "optionValue" : "thisVal",
#             "waitTime" : 10,
#             "description" : "click on button"
#         }
#     ]
# }