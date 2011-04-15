import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from rattus.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HuntController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/hunt.mako')
        # or, return a string
        return 'Hello World'

    def 
