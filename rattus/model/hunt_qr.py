from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, Text

from rattus.model.meta import Base
from rattus.model.qr import QR
from rattus.model.hunt import Hunt

class HuntQR(Base):
    __tablename__ = "hunt_qr"

    id = Column(Integer, primary_key=True)
    hunt_id = Column(Integer, ForeignKey('hunt.id'))
    qr_id = Column(Integer, ForeignKey('qr.id'))
    color = Column(String(16))
    name = Column(Text())
    description = Column(Text())
    secret = Column(Text())
    location = Column(Text())
    order = Column(Integer)

    def __init__(self, hunt_id, qr_id, name, color="FF0000", description='', secret='', location='', order=0):
        self.hunt_id = hunt_id
        self.qr_id = qr_id
        self.name = name
        self.color = color
        self.description = description
        self.secret = secret
        self.location = location
        self.order = order

    def __repr__(self):
        return "<HuntQR('%s: %d, %d')" % (self.name, self.hunt_id, self.qr_id)
