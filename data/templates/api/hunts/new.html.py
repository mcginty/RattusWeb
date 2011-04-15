# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1302854506.1168909
_template_filename='/var/pylons/rattus/rattus/templates/api/hunts/new.html'
_template_uri='/api/hunts/new.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!doctype html>\n\n<html>\n\t<head>\n\t\t<title>New Hunt</title>\n\t</head>\n\t<body>\n\t\t<form id="new_hunt" name="new_hunt" action="/hunts/create" method="post">\n\t\t\t<fieldset>\n\t\t\t\t<legend>New Hunt</legend>\n\t\t\t\t<label for="name">Name</label><input type="text" name="name" /><br />\n\t\t\t\t<label for="description">Description</label><input type="description" name="description" /><br />\n\t\t\t\t<input type="submit" />\n\t\t\t</fieldset>\n\t\t</form>\n\t</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


