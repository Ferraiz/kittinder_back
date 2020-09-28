import random

from flask import request

from helpers.build_response import build_response
from helpers.random_names import random_names
from models.kitty_model import KittyModel


def get_kitty():
    kitty_from_db = _get_random_kitty_from_db()
    kitty_from_cataas = _get_random_kitty_from_cataas()
    kitty = random.choice([kitty_from_db, kitty_from_cataas])
    if not kitty:
        kitty = _get_random_kitty_from_cataas()
    response = build_response(kitty)
    return response


def _get_random_kitty_from_db():
    kitties_from_db = KittyModel.get_all_kitties()
    random_kitty = random.choice(kitties_from_db)
    response = {'name': f'{random_kitty.name}',
                'photo': f'{random_kitty.photo}'}
    return response


def _get_random_kitty_from_cataas():
    url = 'https://cataas.com/cat'
    random_kitty = request.url
    random_kitty_name = random.choice(random_names)
    response = {'name': f'{random_kitty_name}',
                'url': f'{url}'}
    return response
