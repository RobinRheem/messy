from sanic import Sanic
from sanic.response import json

from messy.chatroom.views import chatrooms
from messy.member.views import members


app = Sanic()
# Add blueprints
blueprints = [
    chatrooms,
    members
]
for blueprint in blueprints:
    app.blueprint(blueprint)


@app.route('/')
async def root(request):
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

