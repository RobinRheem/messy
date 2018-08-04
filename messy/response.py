from sanic.response import json


def json_response(data):
    return json({ 'data': data })

