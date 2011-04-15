from sqlalchemy import Column
from sqlalchemy.types import String, Integer, Text

from rattus.model.meta import Base

class Hunt(Base):
    __tablename__ = "hunt"

    id = Column(Integer, primary_key=True)
    name = Column(Text())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Hunt('%s')" % self.name
