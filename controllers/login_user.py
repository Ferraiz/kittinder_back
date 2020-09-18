from datetime import timedelta

from flask import Response
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import safe_str_cmp

from models.user_model import UserModel


def login_user(user_data):
    user_email = user_data['email']
    user = UserModel.find_by_email(user_email)
    if user and safe_str_cmp(user.password, user_data['password']):
        expires = timedelta(seconds=60)
        access_token = create_access_token(
            identity=user.email, expires_delta=expires)
        response = Response(
            f'access_token: {access_token} expires in {expires}. User id: {user.id}.')
        return response
    response = Response('Invaild credentials.', 403)
    return response
