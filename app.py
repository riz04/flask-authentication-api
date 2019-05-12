from flask import Flask,request

# resources are things that Api can return and create
# e.g, if an api is concerned with an item, then item can be the resource
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = "rizulgit"

# api will allow us to add resources to it
# the API works with resources, and every resource has to be a class
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


# inheriting class student from Resource
class Item(Resource):
    # this decorator ensures that we authenticate before get responds
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item["name"] == name:
        #         return item

        item = next(filter(lambda x : x["name"] == name, items) , None)
        return item, 200 if item else 404

    def post(self, name):
        error_message = {"message" : "An item with name '{}' already exists.".format(name)}
        if next(filter(lambda x : x["name"] == name, items) , None) is  not None:
            return error_message, 400


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