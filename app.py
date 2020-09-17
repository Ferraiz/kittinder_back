from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Resource, Api

from db import db
from resources.info_resources import Info
from resources.user_resources import User, UserLogin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
api = Api(app)
app.config['JWT_SECRET_KEY'] = 'marramiau'
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Info, '/info')
api.add_resource(User, '/user')
api.add_resource(UserLogin, '/login')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
