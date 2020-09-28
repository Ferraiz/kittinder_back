from helpers.build_response import build_response
from helpers.get_user_kitties import get_user_kitties


def get_kitties(user_id):
    # ¿Debería comprobar si existe el usuario?
    kitties = get_user_kitties(user_id)
    if not kitties:
        response = build_response(
            {'error message': 'This user has no kitties yet'}, 404)
        return response
    response = build_response(kitties)
    return response
