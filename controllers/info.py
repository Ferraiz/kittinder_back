from controllers.build_response import build_response


def get_info():
    name = 'Kittinder'
    version = '1.0'
    response = build_response({'name': f'{name}', 'version': f'{version}'})
    return response
