from flask import Response


def get_info():
    info = '{name: "Kittinder", version: "1.0"}'
    response = Response(info)
    return response
