import logging
from simplejson import dumps
import urllib2
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from rattus.model.meta import Session
from rattus.model.qr import QR
from rattus.model.hunt_codes import HuntCodes
from rattus.lib.base import BaseController, render

log = logging.getLogger(__name__)

class TargetsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""

    def index(self, format='html'):
        """GET /targets: All items in the collection"""
        # url('targets')
        d = {}
        d['targets'] = []
        for target in Session.query(HuntCodes).all():
            d['targets'].append( {
                    'id': target.id,
                    'name': target.name,
                    'color': target.color,
                    } )
        return dumps(d)


    def create(self):
        """POST /targets: Create a new item"""
        # url('targets')
        newqr = QR()
        Session.add(newqr)
        Session.flush()
        newtarget = HuntCode(0, newqr.id, request.params['name'], request.params['color'], request.params['description'], request.params['secret'], request.params['location'], int(request.params['order']))
        Session.add(newtarget)
        Session.commit()
        response.headers['Content-type'] = 'image/png'
        qr = urllib2.urlopen('http://chart.apis.google.com/chart?chs=480x480&cht=qr&chld=|0&chl='+str(newtarget.id)).read()
        return qr


    def new(self, format='html'):
        """GET /targets/new: Form to create a new item"""
        # url('new_target')
        return "<html><body><form method=post action=/targets/create>name: <input name=name /><br />color: <input name=color /><br />description: <input name=description /><br />secret: <input name=secret /><br />location: <input name=location /><br />order#: <input type=number name=order /><br /><input type=submit></form></body></html>"

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
        target = Session.query(Target).filter(Target.id==id).all()
        if len(target) == 0:
            d = {
                    'valid': False
                }
            return dumps(d)

        d = {
                'valid': True,
                'name': target[0].name,
                'color': target[0].color,
                'qr': 'http://chart.apis.google.com/chart?chs=480x480&cht=qr&chld=|0&chl='+str(target[0].id),
                }
        return dumps(d)

    def edit(self, id, format='html'):
        """GET /targets/id/edit: Form to edit an existing item"""
        # url('edit_target', id=ID)
