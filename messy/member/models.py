from messy import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey


class ChatroomMember(Base):
    __tablename__ = 'chatroom_members'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    chatroom_id = Column(Integer, ForeignKey('chatrooms.id'))
    notification = Column(Boolean)
    role = Column(String(50))
    updated_at = Column(DateTime)
    created_at = Column(DateTime)

