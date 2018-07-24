from sanic import Blueprint


members = Blueprint('members', url_prefix='/api/v1/chatrooms/<int:chatroom_id>/members')

