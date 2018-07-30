from messy import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship


class Chatroom(Base):
    __tablename__ = 'chatrooms'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    member_limit = Column(Integer)
    private = Column(Boolean)
    password = Column(String)
    type = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)
    deleted_at = Column(DateTime)
    members = relationship("ChatroomMember")
    messages = relationship("ChatroomMessage")


class ChatroomMessage(Base):
    __tablename__ = 'chatroom_messages'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    chatroom_id = Column(Integer, ForeignKey('chatrooms.id'))
    message = Column(Text)
    type = Column(String)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

