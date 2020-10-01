from helpers.build_response import build_response


def get_info():
    name = 'Kittinder'
    version = '1.0'
    response = build_response({'name': name, 'version': version})
    return response
