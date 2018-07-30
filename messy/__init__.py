from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# This is for alembic to get the metadata from the base
from .chatroom.models import *
from .member.models import *

