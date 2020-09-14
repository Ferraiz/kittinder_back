from flask import Flask
from flask_restful import Resource, Api

from resources.info_resources import Info

app = Flask(__name__)
api = Api(app)

api.add_resource(Info, '/info')

if __name__ == '__main__':
    app.run(debug=True)
