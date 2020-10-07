from helpers.build_response import build_response
from models.favourites_model import FavouritesModel


def post_fav(fav_data, user_id):
    if not fav_data:
        response = build_response({'error message': 'Wrong data format'}, 400)
        return response
    fav_name = fav_data['name']
    if fav_data['photo']:
        fav_image = fav_data['photo']
        source = 'photo'
        favourite = FavouritesModel(
            kitty_name=fav_name, user_id=user_id, photo=fav_image)
        favourite.save()
    elif fav_data['url']:
        fav_image = fav_data['url']
        source = 'url'
        favourite = FavouritesModel(
            kitty_name=fav_name, user_id=user_id, url=fav_image)
        favourite.save()
    else:
        response = build_response(
            {'error message': 'inform "url" or "photo"'}, 400)
        return response
    response = build_response({'name': fav_name, source: fav_image})
    return response
