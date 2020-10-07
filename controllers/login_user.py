from datetime import timedelta
import os


from helpers.build_response import build_response
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import safe_str_cmp

from models.user_model import UserModel


def login_user(user_data):
    user_email = user_data['email']
    expires = timedelta(seconds=int(os.environ.get('EXPIRE_TIME', '1200')))
    user = UserModel.find_by_email(user_email)
    if user and safe_str_cmp(user.password, user_data['password']):
        access_token = create_access_token(
            identity=user.id, expires_delta=expires)
        response = build_response({'token': access_token})
        return response
    response = build_response({'error message': 'Invalid credentials'}, 403)
    return response
