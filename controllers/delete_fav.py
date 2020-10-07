from helpers.build_response import build_response
from models.favourites_model import FavouritesModel


def delete_fav(user_id, fav_id):
    favourite = FavouritesModel.find_by_id(fav_id)
    user_favs = FavouritesModel.find_by_user(user_id)
    if favourite not in user_favs:
        response = build_response(
            {'error message': 'Favourite kitty not found'}, 404)
        return response
    favourite.delete()
    response = build_response({'message': 'Favourite kitty deleted'})
    return response
