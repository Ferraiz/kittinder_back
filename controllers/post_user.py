from flask import request, Response


from db import db
from models.user_model import UserModel
from schemas.user_schema import UserSchema

user_schema = UserSchema()


def post_user():
    json_data = request.get_json()
    if not json_data:
        response = Response('Wrong data format', 400)
        return response
    data = user_schema.load(json_data)
    user_email, user_password = data['email'], data['password']
    if UserModel.find_by_email(user_email):
        response = Response('Email already exists', 409)
        return response
    user = UserModel(user_email, user_password)
    print(user.email)
    db.session.add(user)
    db.session.commit()
    response = Response(f'{{email: {user.email}}}')
    return response

    # curl -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/user


# def get_user():
#     return 'user'
