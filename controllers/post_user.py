from flask import request, Response

from models.user_model import UserModel
from schemas.user_schema import UserSchema

user_schema = UserSchema()


def post_user():
    if UserModel.find_by_email(email):
        response = Response('Email already exists', 409)
    json_data = request.get_json()
    if not json_data:
        response = Response('Body mal formado', 400)
        return response
    data = user_schema.load(json_data)
    user_email, user_password = data['user']['email'], data['user']['password']
    user = UserModel(user_email, user_password)
    db.session.add(user)
    db.session.commit()
    response = Response(f'{{email: {user.user_email}}}')
    return response
