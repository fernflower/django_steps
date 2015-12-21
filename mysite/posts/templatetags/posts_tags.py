import functools

from pyquery import PyQuery
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse


class CutNode(template.Node):
    """Cuts text that is longer than settings.TEXT_CHARS_COUNT.

    If after text has been cut more than 2 images or iframes remain, the rest
    are cut as well.
    """

    def __init__(self, html, post_id=None):
        self.html = html
        self.post_id = post_id

    def render(self, context):
        def gen_cut_url():
            if self.post_id:
                post_id = template.Template(self.post_id).render(context)
                return ("<a href='%(url)s'>%(cut_text)s</a>" %
                        {'url': reverse('posts:detail', kwargs={'pk': post_id}),
                         'cut_text': settings.HTML_CUT_TEXT})
            return None

        has_been_cut = False
        t = template.Template(self.html)
        rendered_html = t.render(context)
        pq = PyQuery(PyQuery(rendered_html).html())
        # find tag that overflows allowed chars counter
        tags = pq.children()
        final_tag = next(
            (tag for tag in tags
                if sum(len(t.text) for t in tags[:tags.index(tag) + 1]
                       if t.text) > settings.TEXT_CHARS_COUNT), None)
        if final_tag:
            for tag in tags[tags.index(final_tag):]:
                parent = tag.getparent()
                parent.remove(tag)
            has_been_cut = True
        images = functools.reduce(lambda x, img_list: x.extend(img_list),
                                  [p.xpath('//img|iframe') for p in pq])
        if len(images) > settings.IMG_VIDEO_COUNT:
            remove_tag = images[settings.IMG_VIDEO_COUNT - 1]
            # remove all tags after final
            while remove_tag is not None:
                # find parent tag and remove element from it
                remove_parent = remove_tag.getparent()
                next_remove_tag = remove_tag.getnext()
                remove_parent.remove(remove_tag)
                remove_tag = next_remove_tag
            has_been_cut = True
        if has_been_cut and gen_cut_url():
            pq.append(gen_cut_url())
        return pq.outer_html()


def do_cut(parser, token):
    try:
        tag_name, html, post_id = token.split_contents()
        return CutNode(html, post_id)
    except ValueError:
        raise template.TemplateSyntaxError(
            "{%s} tag requires a single argument" % token.contents.split()[0])


register = template.Library()
register.tag('cut_html', do_cut)
