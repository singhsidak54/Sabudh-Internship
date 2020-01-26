from flask import Flask, request, abort, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:MongoAdmin@cluster0-jaely.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/signup", methods=["POST"])
def signup():

    user = {
        'username': request.json['username'],
        'password': request.json['password'],
        'email': request.json['email']
        }

    users = mongo.db.users

    users.insert(user)

    return jsonify({'status': 200, "response_message": "user " + request.json['username'] + " sign up successfully"})

@app.route("/login",methods=["POST"])
def login():

    user = {
        'username': request.json['username'],
        'password': request.json['password']
        }

    users = mongo.db.users

    res = users.find_one(user)

    if res:
        return jsonify({'status': 200, "response": {"username" : res['username'], "useremail": res['email']}})
    else:
        return jsonify(({"status":404, "response_message": "Invalid details."}))



if __name__ == '__main__':
    app.run(debug=True)