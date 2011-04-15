from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, Text

from rattus.model.meta import Base

class HuntCodes(Base):
    __tablename__ = "hunt_codes"

    id = Column(Integer, primary_key=True)
    hunt_id = Column(Integer, ForeignKey('hunt.id'))
    qr_id = Column(Integer, ForiegnKey('qr.id'))
    color = Column(String(16))
    name = Column(Text())
    description = Column(Text())
    secret = Column(Text())
    location = Column(Text())
    order = Column(Integer)

    def __init__(self, hunt_id, qr_id, color=(255, 0, 0), name, description='', secret='', location='', order=0):
        self.hunt_id = hunt_id
        self.qr_id = qr_id
        self.color = str(color)
        self.name = name
        self.description = description
        self.secret = secret
        self.location = location
        self.order = order

    def __repr__(self):
        return "<HuntCode('%s: %d, %d')" % (self.name, self.hunt_id, self.qr_id)
