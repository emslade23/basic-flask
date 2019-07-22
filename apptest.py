from flask import Flask, render_template, Api, Resource, reqparse

app = Flask(__name__)

api = Api(app)

@app.route("/")
def welcomePage():
    return render_template("welcome.html")

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

# User Resource Class
class User(Resource):
    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
            else:
                return "User not found", 404
    
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age") # adds arguments to be parsed
        parser.add_argument("occupation")

        args = parser.parse_args() # parses arguments

        for user in users:
            if name == user["name"]:
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age" : args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
        

    def put(self, name):

    def delete(self, name):

    