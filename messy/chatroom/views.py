from sanic import Blueprint
from messy.base import scoped_session
from messy.response import json_response
from messy.chatroom.models import Chatroom


chatrooms = Blueprint('chatrooms', url_prefix='/api/v1/chatrooms')


@chatrooms.get('/')
async def chatroom_list(request):
    pass


@chatrooms.get('/<chatroom_id:int>')
async def chatroom(request, chatroom_id):
    pass


@chatrooms.post('/')
async def create(request):
    pass


@chatrooms.put('/<chatroom_id:int>')
async def update(request, chatroom_id):
    pass


@chatrooms.delete('/<chatroom_id:int>')
async def delete(request, chatroom_id):
    pass

