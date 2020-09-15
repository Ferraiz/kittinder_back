from flask import Response


from db import db
from facades.user_validation import user_facade
from models.user_model import UserModel


def post_user(user_data):
    if not user_data:
        response = Response('Wrong data format', 400)
        return response
    user_email, user_password = user_data['email'], user_data['password']
    if not user_facade.email_validation(user_email):
        response = Response('Email has an incorrect format', 400)
        return response
    if UserModel.find_by_email(user_email):
        response = Response('Email already exists', 409)
        return response
    user = UserModel(user_email, user_password)
    user.save()
    response = Response(f'{{email: {user.email}}}')
    return response


# def get_user():
#     return 'user'
