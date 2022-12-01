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
# curl -d "{ \"email\" : \"foo@bar\" }" -X POST http://localhost:9000/check
#
@app.route("/check", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    email = request.json['email']
    number_of_at_signs = email.count("@")

    returnDictionary = {}
    returnDictionary["email"] = email
    returnDictionary["at_signs"] = number_of_at_signs

    if number_of_at_signs == 1:
        returnDictionary["success"] = True
    else:
        returnDictionary["success"] = False    
    
    return json.dumps(returnDictionary)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
