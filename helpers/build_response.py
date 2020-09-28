import json

from flask import Response


def build_response(message, status=200):
    response = Response(json.dumps(message), status)
    response.headers['Content-Type'] = 'application/json'
    return response
