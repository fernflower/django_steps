from pyquery import PyQuery
from django import template
from django.conf import settings
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
        img_video_count = 0
        text_chars_count = 0
        first_clear = True
        pq = PyQuery(pq.html())
        for tag in pq.children():
            text_chars_count += len(tag.text) if tag.text else 0
            if tag.tag == 'img' or tag.tag == 'div' and \
                    tag.get('class') == 'responsive-video':
                img_video_count += 1
            if img_video_count > settings.IMG_VIDEO_COUNT or \
                    text_chars_count > settings.TEXT_CHARS_COUNT:
                parent = tag.getparent()
                parent.remove(tag)
                # add '...' to show that more data is hidden under cut
                if first_clear:
                    first_clear = False
                    pq.append("<a href='{}'>(Узнать больше)</a>".format(
                        reverse('posts:detail', kwargs={'pk': post_id})))
        return pq.outer_html()


register = template.Library()
register.tag('cut_images', do_cut_images)
