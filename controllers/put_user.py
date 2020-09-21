from flask import Response

from facades.user_validation import user_facade
from models.user_model import UserModel


def put_user(user_data, user_id):
    user = UserModel.find_by_id(user_id)  # Buscamos el user por id
    if user:  # Si existe ese user
        # Comprobamos si existe ya un user con ese email
        user_email = UserModel.find_by_email(user_data['email'])
        if not user_email:  # Si el email está disponible: machacamos los datos
            if not user_facade.email_validation(user_data['email']):
                response = Response('Email has an incorrect format', 400)
                return response
            user.email = user_data['email']
            user.password = user_data['password']
        else:  # El email NO está disponible: devolvemos un error 409
            response = Response('Email alrady exists', 409)
            return response
    else:  # Si no existe ese user, devolvemos un error 404
        response = Response('User not found', 404)
        return response

    user.save()  # Guardo la información

    response = Response(f'{{email: {user.email}}}')
    return response
