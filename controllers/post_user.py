from helpers.build_response import build_response
from facades.user_validation import user_facade
from models.user_model import UserModel


def post_user(user_data):
    if not user_data:
        response = build_response({'error message': 'Wrong data format'}, 400)
        return response
    user_email, user_password = user_data['email'], user_data['password']
    if not user_facade.email_validation(user_email):
        response = build_response(
            {'error message': 'Email has an incorrect format'}, 400)
        return response
    if UserModel.find_by_email(user_email):
        response = build_response(
            {'error message': 'Email already exists'}, 409)
        return response
    user = UserModel(user_email, user_password)
    user.save()
    response = build_response({'email': f'{user.email}'})
    return response
