from pyquery import PyQuery
from django import template


def do_cut_images(parser, token):
    try:
        tag_name, html = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "{} tag requires a single argument".format(token.contents.split()[0]))
    return CurrentHtmlNode(html)


class CurrentHtmlNode(template.Node):
    def __init__(self, html):
        self.html = html

    def render(self, context):
        result = super(CurrentHtmlNode, self).render(context)
        t = template.Template(self.html)
        rendered_html = t.render(context)
        pq = PyQuery(rendered_html)
        occurences = pq('img')
        if len(occurences) > 2:
            for img in occurences[2:]:
                img.clear()
        result_html = pq.html()
        return result_html


register = template.Library()
register.tag('cut_images', do_cut_images)
