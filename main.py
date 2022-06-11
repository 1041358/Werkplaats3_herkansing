from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Gamelist(Resource):
    def get(self):
        return {"data": "Game lijst"}
    
    def post(self):
        return {"data": "posted"}


api.add_resource(Gamelist, "/gamelist/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)


