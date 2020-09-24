from controllers.build_response import build_response
from models.user_model import UserModel


def get_user(user_email):
    user = UserModel.find_by_email(user_email)
    if not user:
        response = build_response({'error message': 'User not found'}, 404)
        return response
    response = build_response({'mail': f'{user.email}'})
    return response
