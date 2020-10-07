from helpers.build_response import build_response
from models.kitty_model import KittyModel


def get_kitties(user_id, limit, page):
    kitties = KittyModel.query.filter_by(
        user_id=user_id).paginate(page=page, max_per_page=limit)
    total = kitties.total
    offset = ((page - 1) * limit)
    if not kitties:
        response = build_response(
            {'error message': 'This user has no kitties yet'}, 404)
        return response
    data = dict()
    for kitty in kitties.items:
        data[kitty.name] = kitty.serialize_kitty()
    response = build_response(
        {'offset': offset, 'limit': limit, 'total': total, 'data': data})
    return response
