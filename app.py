from flask import Flask,request

# resources are things that Api can return and create
# e.g, if an api is concerned with an item, then item can be the resource
from flask_restful import Resource, Api

app = Flask(__name__)

# api will allow us to add resources to it
# the API works with resources, and every resource has to be a class
api = Api(app)

items = []


# inheriting class student from Resource
class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
        invalid_item = {"name" : None , "price" : 00.00}
        return invalid_item, 404

    def post(self, name):
        data = request.get_json()
        print(data)
        item = {"name" : name , "price" : data["price"]}
        items.append(item)
        # we need to return this item, so that application knows that something has happened
        # 201 status code represents, something has been created
        return item, 201

class ItemList(Resource):
    def get(self):
        return {"items" : items}

# this resource item which we created, can be accessed via our API
api.add_resource(Item , "/item/<string:name>")
api.add_resource(ItemList , "/items")

app.run(port = 5000, debug = True)