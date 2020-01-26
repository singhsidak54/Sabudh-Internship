from flask import Flask, request, abort, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:MongoAdmin@cluster0-jaely.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/items", methods=["POST"])
def insert():

    item = {
        'name': request.json['name'],
        'description': request.json['description'],
        'cost': request.json['cost'],
        'supplier': request.json['supplier']
        }

    items = mongo.db.items

    items.insert(item)

    return jsonify({'status': 200, "response_message": "uploaded the details successfully"})

@app.route("/items",methods=["GET"])
def fetch():

    items = mongo.db.items

    res = items.find()
   # res = res.toString()
    item_details = []

    for item in res:
        name = item['name']
        description = item['description']
        cost = item['cost']
        supplier = item['supplier']
        item_details.append({'name':name, 'description':description,'cost':cost,'supplier':supplier})
    return jsonify({'status': 200,'item_details':item_details})



if __name__ == '__main__':
    app.run(debug=True)