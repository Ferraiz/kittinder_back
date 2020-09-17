from flask import request, Response
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from controllers.login_user import login_user
from controllers.post_user import post_user  # , get_user
from controllers.put_user import put_user
from models.user_model import UserModel
from schemas.user_schema import UserSchema

user_schema = UserSchema()


class CreateUser(Resource):
    def post(self):
        json_data = request.get_json()
        print(json_data)
        try:
            data = user_schema.load(json_data)
        except:
            return Response('Bad request', 400)
        response = post_user(data)
        return response


class ChangeUser(Resource):
    def put(self, user_id):
        json_data = request.get_json()
        try:
            data = user_schema.load(json_data)
        except:
            return Response('Bad request', 400)
        response = put_user(data, user_id)
        return response

        # user = UserModel.find_by_id(user_id)  # Buscamos el user por id
        # if user:  # Si existe ese user
        #     # Comprobamos si existe ya un user con ese email
        #     user_email = UserModel.find_by_email(data['email'])
        #     if not user_email:  # El email está disponible: machacamos los datos
        #         user.email = data['email']
        #         user.password = data['password']
        #     else:  # El email NO está disponible: devolvemos un error 409
        #         response = Response('Email alrady exists', 409)
        #         return response
        # else:  # Si no existe ese user, devolvemos un error 404
        #     response = Response('User not found', 404)
        #     return response

        # user.save()  # Guardo la información

        # response = Response(f'{{email: {user.email}}}')
        # return response

        # def get(self):
        #     response = get_user()
        #     return response


class UserLogin(Resource):
    def post(self):
        json_data = request.get_json()
        try:
            data = user_schema.load(json_data)
        except:
            return Response('Bad request', 400)
        response = login_user(data)
        return response
