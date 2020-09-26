from controllers.build_response import build_response
from models.kitty_model import KittyModel


def get_kitties(user_id):
    kitties = KittyModel.find_by_user(user_id)
    if not kitties:
        response = build_response(
            {'error message': 'This user has no kitties yet'}, 404)
        return response
    kitties_dict = {}
    for kitty in kitties:
        kitties_dict[kitty.name] = kitty.serialize_kitty()
    response = build_response(kitties_dict)
    return response
