from pyquery import PyQuery
from django import template
from django.core.urlresolvers import reverse


def do_cut_images(parser, token):
    try:
        tag_name, html, post_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "{} tag requires a single argument".format(token.contents.split()[0]))
    return CurrentHtmlNode(html, post_id)


class CurrentHtmlNode(template.Node):
    def __init__(self, html, post_id):
        self.html = html
        self.post_id = post_id

    def render(self, context):
        result = super(CurrentHtmlNode, self).render(context)
        t = template.Template(self.html)
        post_id = template.Template(self.post_id).render(context)
        rendered_html = t.render(context)
        pq = PyQuery(rendered_html)
        img_count = 0
        first_clear = True
        pq = PyQuery(pq.html())
        for tag in pq.children():
            if tag.tag == 'img':
                img_count += 1
            if img_count > 2:
                # TODO perhaps not the most easy way to remove tag
                tag.clear()
                tag.drop_tag()
                # add '...' to show that more data is hidden under cut
                if first_clear:
                    first_clear = False
                    pq.append("<a href='{}'>(Узнать больше)</a>".format(
                        reverse('posts:detail', kwargs={'pk': post_id})))
        return pq.outer_html()


register = template.Library()
register.tag('cut_images', do_cut_images)
