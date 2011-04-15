# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1302858648.752552
_template_filename='/var/pylons/rattus/rattus/templates/api/codes/new.html'
_template_uri='/api/codes/new.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!doctype html>\n\n<html>\n\t<head>\n\t\t<title>New Hunt</title>\n\t</head>\n\t<body>\n\t\t<form id="new_hunt" name="new_hunt" action="/codes/create" method="post">\n\t\t\t<fieldset>\n\t\t\t\t<legend>New QR</legend>\n\t\t\t\t<label for="hunt">Hunt</label>\n\t\t\t\t<select name="hunt">\n')
        # SOURCE LINE 13
        for hunt in c.hunts:
            # SOURCE LINE 14
            __M_writer(u'\t\t\t\t\t<option value="')
            __M_writer(escape(hunt[0]))
            __M_writer(u'">')
            __M_writer(escape(hunt[1]))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 16
        __M_writer(u'\t\t\t\t</select><br />\n\t\t\t\t<label for="name">Name</label><input type="text" name="name" /><br />\n\t\t\t\t<label for="description">Description</label><input type="text" name="description" /><br />\n\t\t\t\t<label for="color">Color</label><input type="text" name="color" /><br />\n\t\t\t\t<label for="secret">Secret</label><input type="text" name="secret" /><br />\n\t\t\t\t<label for="location">Location</label><input type="text" name="location" /><br />\n\t\t\t\t<label for="order">Order</label><input type="text" name="order" /><br />\n\t\t\t\t<input type="submit" />\n\t\t\t</fieldset>\n\t\t</form>\n\t</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


