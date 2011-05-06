# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1304498893.2734621
_template_filename='/var/pylons/rattus/rattus/templates/api/userhunt/new.html'
_template_uri='/api/userhunt/new.html'
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
        __M_writer(u'<!doctype html>\n\n<html>\n    <head>\n        <title>New Hunt</title>\n    </head>\n    <body>\n        <form id="new_hunt" name="new_hunt" action="/codes/create" method="post">\n            <fieldset>\n                <legend>New QR</legend>\n                <label for="hunt">Hunt</label>\n                <select name="hunt">\n')
        # SOURCE LINE 13
        for hunt in c.hunts:
            # SOURCE LINE 14
            __M_writer(u'                    <option value="')
            __M_writer(escape(hunt[0]))
            __M_writer(u'">')
            __M_writer(escape(hunt[1]))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 16
        __M_writer(u'                </select><br />\n                <label for="">User</label>\n                <select name="user">\n')
        # SOURCE LINE 19
        for user in c.users:
            # SOURCE LINE 20
            __M_writer(u'                    <option value="')
            __M_writer(escape(user[0]))
            __M_writer(u'">')
            __M_writer(escape(user[1]))
            __M_writer(u'</option>\n')
            pass
        # SOURCE LINE 22
        __M_writer(u'                </select><br />\n                <input type="submit" />\n            </fieldset>\n        </form>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


