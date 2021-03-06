import logging
from json import dumps
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from rattus.model.meta import Session
from rattus.lib.base import BaseController, render
from rattus.model.hunt import Hunt
from rattus.model.qr import QR
from rattus.model.hunt_qr import HuntQR

log = logging.getLogger(__name__)

class HuntsController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('hunt', 'hunts')

    def index(self, format='html'):
        """GET /hunts: All items in the collection"""
        # url('hunts')
        d = []
        for hunt in Session.query(Hunt).all():
            d.append({'name': hunt.name, 'description': hunt.description})
        return dumps(d)

    def create(self):
        """POST /hunts: Create a new hunt"""
        # url('hunts')
        if 'name' in request.params and 'description' in request.params:
            hunt = Hunt(request.params['name'], request.params['description'])
            Session.add(hunt)
            Session.commit()
            d = {
                    'status': 'ok',
                    'message': 'Successfully created hunt "%s"' % request.params['name'],
                }
        else:
            d = {
                    'status': 'failure',
                    'message': 'Name and description not posted.'
                }
        return dumps(d)

    def new(self, format='html'):
        """GET /hunts/new: Form to create a new item"""
        # url('new_hunt')

    def update(self, id):
        """PUT /hunts/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('hunt', id=ID),
        #           method='put')
        # url('hunt', id=ID)

    def delete(self, id):
        """DELETE /hunts/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('hunt', id=ID),
        #           method='delete')
        # url('hunt', id=ID)

    def show(self, id, format='html'):
        """GET /hunts/id: Show a specific item"""
        # url('hunt', id=ID)

    def edit(self, id, format='html'):
        """GET /hunts/id/edit: Form to edit an existing item"""
        # url('edit_hunt', id=ID)
