from controllers.build_response import build_response


def get_info():
    info = '{name: "Kittinder", version: "1.0"}'
    response = build_response(info)
    return response
