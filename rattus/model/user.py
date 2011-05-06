from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, Text, DateTime

from rattus.model.meta import Base
from rattus.model.qr import QR
from rattus.model.hunt import Hunt

class HuntQR(Base):
    __tablename__ = "hunt_qr"

    id = Column(Integer, primary_key=True)
    username = Column(Text())
    password = Column(Text())
    email = Column(Text())

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<HuntQR('%s: %d, %d')" % (self.name, self.hunt_id, self.qr_id)
