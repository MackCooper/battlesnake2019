import json
import os
import bottle
import pprint

import api
import obj
from logic import logic

pp = pprint.PrettyPrinter(indent=4)

@bottle.post('/ping')
def ping():
    return api.ping_response()

@bottle.post('/start')
def start():
    data = bottle.request.json
    # pp.pprint(data)
    #color = "#f1f1f1"
    color = "#ff0000"
    return api.start_response(color)

@bottle.post('/move')
def move():
    data = obj.Data(bottle.request.json)
    # print(data)
    direction = logic(data)
    return api.move_response(direction)

@bottle.post('/end')
def end():
    data = bottle.request.json
    # pp.pprint(data)
    return api.end_response()

application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )
