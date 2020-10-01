from helpers.build_response import build_response
from facades.cat_validation import cat_facade
from models.kitty_model import KittyModel


def post_kitty(kitty_data, user_id):
    if not kitty_data:
        response = build_response({'error message': 'Wrong data format'}, 400)
        return response
    kitty_name, kitty_photo = kitty_data['name'], kitty_data['photo']
    if not cat_facade.name_validation(kitty_name):
        response = build_response({'error message': 'Name is empty'}, 400)
        return response
    if KittyModel.find_by_name(kitty_name):
        response = build_response(
            {'error message': 'Name already exists'}, 409)
        return response
    kitty = KittyModel(kitty_name, kitty_photo, user_id)
    kitty.save()
    response = build_response(
        {'name': kitty_name, 'photo': kitty_photo})
    return response
