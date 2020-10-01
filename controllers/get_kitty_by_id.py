from helpers.build_response import build_response
from helpers.get_user_kitties import get_user_kitties
from models.kitty_model import KittyModel
from models.user_model import UserModel


def get_kitty_by_id(user_id, kitty_id):
    kitties_from_db = get_user_kitties(user_id)
    kitty_by_id = KittyModel.find_by_id(kitty_id)
    if kitty_by_id.name not in kitties_from_db:
        response = build_response(
            {'error message': 'Kitty not found'}, 404)
        return response
    user = UserModel.find_by_id(user_id)
    kitty_dict = kitty_by_id.serialize_kitty()
    kitty_dict['user'] = {'id': user_id, 'email': user.email}
    response = build_response(kitty_dict)
    return response
