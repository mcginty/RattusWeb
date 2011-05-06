import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from rattus.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UserhuntController(BaseController):
    """REST Controller styled on the Atom Publishing Protocol"""
    # To properly map this controller, ensure your config/routing.py
    # file has a resource setup:
    #     map.resource('userhunts', 'userhunt')

    def index(self, format='html'):
        """GET /userhunt: All items in the collection"""
        # url('userhunt')

    def create(self):
        """POST /userhunt: Create a new item"""
        # url('userhunt')
        if 'hunt' in request.params and 'phone_id' in request.params:
            userhunt = UserHunt(request.params['hunt'], request.params['user'])
            Session.add(userhunt)
            Session.commit()
            d = {
                    'status': 'ok',
                    'message': 'User %s successfully joined hunt "%s".' % (request.params['user'], request.params['hunt'])
                }
        else:
            d = {
                    'status': 'failure',
                    'message': 'User and Hunt not posted.'
                }
        return dumps(d)

    def new(self, format='html'):
        """GET /userhunt/new: Form to create a new item"""
        # url('new_userhunts')

    def update(self, id):
        """PUT /userhunt/id: Update an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="PUT" />
        # Or using helpers:
        #    h.form(url('userhunts', id=ID),
        #           method='put')
        # url('userhunts', id=ID)

    def delete(self, id):
        """DELETE /userhunt/id: Delete an existing item"""
        # Forms posted to this method should contain a hidden field:
        #    <input type="hidden" name="_method" value="DELETE" />
        # Or using helpers:
        #    h.form(url('userhunts', id=ID),
        #           method='delete')
        # url('userhunts', id=ID)

    def show(self, id, format='html'):
        """GET /userhunt/id: Show a specific item"""
        # url('userhunts', id=ID)

    def edit(self, id, format='html'):
        """GET /userhunt/id/edit: Form to edit an existing item"""
        # url('edit_userhunts', id=ID)
