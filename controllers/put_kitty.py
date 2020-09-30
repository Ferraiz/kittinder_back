from models.kitty_model import KittyModel
from helpers.build_response import build_response
from helpers.get_user_kitties import get_user_kitties


def put_kitty(kitty_data, user_id, kitty_id):
    kitty = KittyModel.find_by_id(kitty_id)
    print(kitty)
    user_kitties = KittyModel.find_by_user(user_id)
    print(user_kitties)
    if kitty not in user_kitties:
        response = build_response({'error message': 'Kitty not found'}, 404)
        return response
    kitty.name = kitty_data['name']
    kitty.photo = kitty_data['photo']
    kitty.save()
    response = build_response({'name': f'{kitty.name}'})
    return response

    # Buscamos el gato y comprobamos que pertenece al usuario
    # Si no pertenece al usuario --> ERROR
    # Si pertenece, se modifica el gato
