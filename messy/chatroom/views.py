from sanic import Blueprint
from sanic.response import json
from messy.base import scoped_session
from messy.chatroom.models import Chatroom


chatrooms = Blueprint('chatrooms', url_prefix='/api/v1/chatrooms')


@chatrooms.get('/')
async def chatroom_list(request):
    with scoped_session() as session:
        response = session.query(Chatroom).first()
        return json({ 'data': dict(response) if response else None })

