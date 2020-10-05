from helpers.build_response import build_response
from models.favourites_model import FavouritesModel


def post_fav(fav_data, user_id):
    if not fav_data:
        response = build_response({'error message': 'Wrong data format'}, 400)
        return response
    fav_name = fav_data['name']
    fav_image = fav_data['image']
    favourite = FavouritesModel(fav_name, fav_image, user_id)
    favourite.save()
    response = build_response({'name': fav_name, 'image': fav_image})
    return response
