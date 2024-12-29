from flask import Flask, json, jsonify, request

app = Flask(__name__)

@app.route('/postUserInput', methods=['POST'])
def postUserInput():
    if request.method == 'POST':
        jsonData = request.get_json()
        # Below checks if jsonData['txnId'] has any value or not, if no value then retuns 402 response
        if not jsonData['txnId']:
            return jsonify({'errorMessage' : 'tnxId is null'}), 402
        if not jsonData['fileName']:
            return jsonify({'errorMessage' : 'fileName is null'}), 402
        if not jsonData['webUrl']:
            return jsonify({'errorMessage' : 'webUrl is null'}), 402
        for action in jsonData['actions']:
            if not action['selectorKey']:
                return jsonify({'errorMessage' : 'selectorKey is null'}), 402
            if not action['selectorValue']:
                return jsonify({'errorMessage' : 'selectorKey is null'}), 402
            if not action['optionKey']:
                return jsonify({'errorMessage' : 'optionKey is null'}), 402
            if not action['description']:
                return jsonify({'errorMessage' : 'description is null'}), 402
            if not action['optionValue']:
                pass
            print(action['selectorKey'])
            print(action['selectorValue'])
            print(action['optionKey'])
            print(action['optionValue'])
            print(action['description'])
        return jsonify({'errorMessage' : 'Success'}), 201
        
if __name__ == '__main__':
    app.run(debug=True, port=8080)

# Below is the body for api, request. action is an array so multiple dictionary could be included

# {
#     "txnId" : "9721628",
#     "fileName" : "chan",
#     "webUrl" : "https://",
#     "actions" : [
#         {
#             "selectorKey" : "Id",
#             "selectorValue" : "someButton",
#             "optionKey" : "something",
#             "optionValue" : "thisVal",
#             "description" : "click on button"
#         },
#         {
#             "selectorKey" : "name",
#             "selectorValue" : "event",
#             "optionKey" : "something",
#             "description" : "click on button"
#         },
#         {
#             "selectorKey" : "link",
#             "selectorValue" : "aref",
#             "optionKey" : "something",
#             "optionValue" : "thisVal",
#             "description" : "click on button"
#         }
#     ]
# }