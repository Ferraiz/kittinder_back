from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from resources.info_resources import Info
from resources.user_resources import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

api.add_resource(Info, '/info')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)
