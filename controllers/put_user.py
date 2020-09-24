from controllers.build_response import build_response
from facades.user_validation import user_facade
from models.user_model import UserModel


def put_user(user_data, user_id):
    user = UserModel.find_by_id(user_id)  # Buscamos el user por id
    if user:  # Si existe ese user
        # Comprobamos si existe ya un user con ese email
        user_email = UserModel.find_by_email(user_data['email'])
        if not user_email:  # Si el email está disponible: machacamos los datos
            if not user_facade.email_validation(user_data['email']):
                response = build_response(
                    {'error message': 'Email has an incorrect format'}, 400)
                return response
            user.email = user_data['email']
            user.password = user_data['password']
        else:  # El email NO está disponible: devolvemos un error 409
            response = build_response(
                {'error message': 'Email alrady exists'}, 409)
            return response
    else:  # Si no existe ese user, devolvemos un error 404
        response = build_response({'error message': 'User not found'}, 404)
        return response

    user.save()  # Guardo la información
    response = build_response({'email': f'{user.email}'})
    return response
