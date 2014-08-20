import re
from django import template

AT_REGEX = re.compile(r"([a-zA-Z0-9\.\-\_]*)\s*@\s*([a-zA-Z0-9\.\-\_]*)")


def do_substitute_at(parser, token):
    try:
        tag_name, email = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "{} tag requires a single argument".format(
                token.contents.split()[0]))
    return CurrentEmailNode(email)


class CurrentEmailNode(template.Node):
    def __init__(self, email):
        self.email = email

    def render(self, context):
        super(CurrentEmailNode, self).render(context)
        email = template.Template(self.email).render(context)
        m = AT_REGEX.match(email)
        if m:
            at_html = template.Template(
                "<img class='icon' src='{{ STATIC_URL }}icons/asterisk_orange.png' />").\
                render(context)
            return m.group(1) + at_html + m.group(2)
        return email


register = template.Library()
register.tag('substitute_at', do_substitute_at)
