"""The application's model objects"""
from rattus.model.meta import Session, Base

from rattus.model.hunt import Hunt
from rattus.model.qr import QR
from rattus.model.hunt_qr import HuntQR

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
