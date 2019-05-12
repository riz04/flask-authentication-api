from flask import Flask

# resources are things that Api can return and create
# e.g, if an api is concerned with an item, then item can be the resource
from flask_restful import Resource, Api

app = Flask(__name__)

# api will allow us to add resources to it
# the API works with resources, and every resource has to be a class
api = Api(app)

# inheriting class student from Resource
class Student(Resource):
    def get(self, name):
        return { "student" : name} 

# this resource student which we created, can be accessed via our API
api.add_resource(Student , "/Student/<string:name>")

app.run(port = 5000, debug = True)