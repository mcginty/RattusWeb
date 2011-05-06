from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, Text

from rattus.model.meta import Base
from rattus.model.qr import QR
from rattus.model.hunt import Hunt

class UserHunt(Base):
    __tablename__ = "user_hunt"

    id = Column(Integer, primary_key=True)
    phone_id = Column(Text())
    hunt_id = Column(Integer, ForeignKey('hunt.id'))
    location = Column(Integer)

    def __init__(self, hunt_id, user_id, location=0):
        self.hunt_id = hunt_id
        self.user_id = user_id
        self.location = location

    def __repr__(self):
        return "<UserHunt(%d, %d, %d)>" % (self.hunt_id, self.user_id, self.location)
