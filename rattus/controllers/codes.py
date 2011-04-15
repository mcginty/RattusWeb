import logging
from json import dumps
import urllib2
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from rattus.model.meta import Session
from rattus.model.hunt import Hunt
from rattus.model.qr import QR
from rattus.model.hunt_qr import HuntQR
from rattus.lib.base import BaseController, render

log = logging.getLogger(__name__)

class CodesController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""

    def index(self, format='html'):
        """GET /targets: All items in the collection"""
        # url('targets')
        d = []
        for qr in Session.query(HuntQR).all():
            d.append( {
                    'qr_id': qr.qr_id,
                    'hunt_id': qr.hunt_id,
                    'name': qr.name,
                    } )
        return dumps(d)


    def create(self):
        """POST /targets: Create a new item"""
        # url('targets')
        newqr = QR()
        Session.add(newqr)
        Session.flush()
        Session.refresh(newqr)
        order = len(Session.query(HuntQR).filter_by(hunt_id=int(request.params['hunt'])).all())
        huntqr = HuntQR(
                int(request.params['hunt']), 
                newqr.id, 
                request.params['name'], 
                request.params['color'], 
                request.params['description'], 
                request.params['secret'], 
                request.params['location'], 
                order)
        Session.add(huntqr)
        Session.commit()
        response.headers['Content-type'] = 'image/png'
        qr = urllib2.urlopen('http://chart.apis.google.com/chart?chs=480x480&cht=qr&chld=|0&chl=http%3A%2F%2Fqrios.me%2F%3A%3A'+str(huntqr.id)).read()
        return qr


    def new(self, format='html'):
        """GET /targets/new: Form to create a new item"""
        # url('new_target')
        # return "<html><body><form method=post action=/targets/create>name: <input name=name /><br />color: <input name=color /><br />description: <input name=description /><br />secret: <input name=secret /><br />location: <input name=location /><br />order#: <input type=number name=order /><br /><input type=submit></form></body></html>"
        hunts = Session.query(Hunt).all()
        c.hunts = []
        for hunt in hunts:
            c.hunts.append( (hunt.id, hunt.name) )
        return render('/api/codes/new.html')

    def update(self, id):
        """PUT /targets/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('target', id=ID),
        #           method='put')
        # url('target', id=ID)

    def delete(self, id):
        """DELETE /targets/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('target', id=ID),
        #           method='delete')
        # url('target', id=ID)

    def show(self, id, format='html'):
        """GET /targets/id: Show a specific item"""
        # url('target', id=ID)
        d = {}
        huntqr = Session.query(HuntQR).filter(HuntQR.id==id).all()
        if len(huntqr) == 0:
            d = {
                    'valid': False
                }
            return dumps(d)

        d = {
                'valid': True,
                'name': huntqr[0].name,
                'color': huntqr[0].color,
                'description': huntqr[0].description,
                'secret': huntqr[0].secret,
                'location': huntqr[0].location,
                'order': huntqr[0].order,
                'qr': 'http://chart.apis.google.com/chart?chs=480x480&cht=qr&chld=|0&chl=http%3A%2F%2Fqrios.me%2F%3A%3A'+str(huntqr[0].id),
                }
        return dumps(d)

    def edit(self, id, format='html'):
        """GET /targets/id/edit: Form to edit an existing item"""
        # url('edit_target', id=ID)
