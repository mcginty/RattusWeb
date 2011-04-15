from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Text

from rattus.model.meta import Base

class Target(Base):
    __tablename__ = "target"

    id = Column(Integer, primary_key=True)
    name = Column(Text())
    color = Column(String(16))

    def __init__(self, name='', color='255,0,0'):
        self.name = name
        self.color = color

    def __repr__(self):
        return "<Target('%s')" % self.name
