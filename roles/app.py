#
#
#
from flask import request, Flask
import json, socket


# import sys
# sys.path.insert(0,"..")

# import my_imports.top


app = Flask(__name__)

emailRoles = {}

#
# curl http://localhost:9002
#
@app.route('/')
def echo():
    returnDictionary = {}
    returnDictionary["echo"] = str(socket.gethostname())
    return json.dumps(returnDictionary)

#
# curl -d '{ "email": "user_email", "newRole" : "role_to_add" }' -X POST http://localhost:9002/addrole  -H "Content-type: application/json"
#
@app.route("/addrole", methods=["POST"])
def addrole():

    user_email = request.json['email']
    new_role = request.json['newRole']    
    
    if user_email not in emailRoles:
    	emailRoles[user_email] = [new_role]
    else:
    	usr_roles_already = emailRoles[user_email] 
    	if new_role not in usr_roles_already:
    		usr_roles_already += [new_role]
   
    return json.dumps(emailRoles)

#
# curl -d '{ "email": "user_email", "remove_role" : "role_to_delete" }' -X POST http://localhost:9002/removerole  -H "Content-type: application/json"
#
@app.route("/removerole", methods=["POST"])
def removerole():

    user_email = request.json['email']
    remove_role = request.json['remove_role']    
    
    if user_email in emailRoles:
    	if remove_role in emailRoles[user_email]:
            emailRoles[user_email].remove(remove_role)

    return json.dumps(emailRoles)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9002)
