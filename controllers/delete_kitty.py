from helpers.build_response import build_response
from models.kitty_model import KittyModel


def delete_kitty(user_id, kitty_id):
    kitty = KittyModel.find_by_id(kitty_id)
    user_kitties = KittyModel.find_by_user(user_id)
    if kitty not in user_kitties:
        response = build_response({'error message': 'Kitty not found'}, 404)
        return response
    kitty.delete()
    response = build_response({'message': 'Kitty deleted'})
    return response
