from helpers.build_response import build_response
from models.favourites_model import FavouritesModel


def get_favourites(user_id, limit, page):
    favourites = FavouritesModel.query.filter_by(
        user_id=user_id).paginate(page=page, max_per_page=limit)
    total = favourites.total
    offset = ((page - 1) * limit)
    if not favourites:
        response = build_response(
            {'error message': 'This user has no favourite kitties yet'}, 404)
        return response
    data = dict()
    for favourite in favourites.items:
        data[favourite.kitty_name] = favourite.serialize_favourite()
    response = build_response(
        {'offset': offset, 'limit': limit, 'total': total, 'data': data})
    return response
