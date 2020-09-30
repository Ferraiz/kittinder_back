from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Resource, Api

from db import db
from resources.info_resources import Info
from resources.user_resources import (
    CreateUser, UpdateUser, GetUser, UserLogin)
from resources.kitty_resources import (
    PostKitty, GetKitties, GetKittyById, GetKitty, UpdateKitty, DeleteKitty)

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
api.add_resource(CreateUser, '/user')  # post
api.add_resource(UpdateUser, '/user/<int:user_id>')  # put
api.add_resource(GetUser, '/user/<string:user_email>')
api.add_resource(PostKitty, '/user/<int:user_id>/kitty')
api.add_resource(UserLogin, '/login')
api.add_resource(GetKittyById, '/user/<int:user_id>/kitty/<int:kitty_id>')
api.add_resource(UpdateKitty, '/user/<int:user_id>/kitty/<int:kitty_id>')
api.add_resource(GetKitties, '/user/<int:user_id>/kitties')
api.add_resource(DeleteKitty, '/user/<int:user_id>/kitty/<int:kitty_id>')
api.add_resource(GetKitty, '/kitty')

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
