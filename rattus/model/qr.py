from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Text

from rattus.model.meta import Base

class QR(Base):
    __tablename__ = "qr"

    id = Column(Integer, primary_key=True)

    def __init__(self):
        pass

    def __repr__(self):
        return "<QR('%s')" % self.name
