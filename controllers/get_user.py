from flask import Response

from models.user_model import UserModel


def get_user(user_email):
    user = UserModel.find_by_email(user_email)
    if not user:
        response = Response('User not found.', 404)
        return response
    response = Response(f'{{mail: {user.email}}}')
    return response
