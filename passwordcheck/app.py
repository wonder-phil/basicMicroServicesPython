#
#
#
from flask import request, Flask
import json, socket


app = Flask(__name__)

#
# curl http://localhost:9000
#
@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d "{ \"password\" : \"xxxxxxxx\" }" -X POST http://localhost:9001/check  -H "Content-type: application/json"
#
@app.route("/check", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    password = request.json['password']
    password_length = len(password)

    returnDictionary = {}
    returnDictionary["password"] = password
    returnDictionary["length"] = password_length

    if password_length >= 5:
        returnDictionary["success"] = True
    else:
        returnDictionary["success"] = False    
    
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9001)
