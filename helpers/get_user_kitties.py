from helpers.build_response import build_response
from models.kitty_model import KittyModel


def get_user_kitties(user_id):
    kitties = KittyModel.find_by_user(user_id)
    kitties_dict = dict()
    for kitty in kitties:
        kitties_dict[kitty.name] = kitty.serialize_kitty()
    return kitties_dict
