from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api

from db import db
from resources.info_resources import Info
from resources.user_resources import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(Info, '/info')
api.add_resource(User, '/user')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
