# -*- coding: utf-8 -*-

import os
import subprocess

from django.conf import settings
from django.core.files import File
import django.http as http
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone

from django_summernote.models import Attachment
from scraper import scraper
from posts.models import Post
from posts import utils

SCRAPER = scraper.VkScraper()


@utils.check_sadmin
def scraper_home(request):
    return render_to_response('posts/scraper.html')


@utils.check_sadmin
def scrape_vk(request):
    count = int(request.GET.get('count', 5))
    offset = int(request.GET.get('offset', 0))
    upload_dir = settings.VK_SCRAPE_DIR

    html = "<html><body>%(msg)s</body></html>"

    try:
        SCRAPER.scrape_wall(count=count, upload_dir=upload_dir, offset=offset,
                            save=True)
        posts = _load_scraped(upload_dir)
        return render_to_response('posts/show_scraped.html',
                                  {'posts': posts},
                                  context_instance=RequestContext(request))
    except subprocess.CalledProcessError as e:
        return http.HttpResponseBadRequest(html % {"msg": e.message})


def _load_scraped(data_dir):
    """Load scraped data from data_dir as Posts.

    Posts are saved with is_visible=False and won't be visible to non-admins.
    After post has been saved into db data is removed from data_dir.
    """
    img_html = "<img src='{}' />"
    text_html = "<p>{}</p>"

    def _get_path(filename=''):
        return os.path.join(data_dir, post_dir_name, filename)

    saved = []
    for post_dir_name in os.listdir(data_dir):
        # post dir name has format postid_pubdate
        text = ""

        pics = [f for f in os.listdir(_get_path()) if f != 'text']
        with open(_get_path('text')) as post_text:
            text = text_html.format(post_text.read())
        [post_id, seconds] = map(lambda x: int(x), post_dir_name.split('_'))
        pubdate = timezone.datetime.utcfromtimestamp(seconds)
        # now add TZ info. We save everything in UTC so TZ=utc
        pubdate = timezone.make_aware(pubdate, timezone.utc)
        title = u"Новость № %s" % post_id
        add_br = False
        for pic in pics:
            add_br = not(pic not in [pics[0], pics[-1]]) or True
            # upload attachments
            attachment = Attachment(name=pic,
                                    file=File(open(_get_path(pic), 'rb')))
            attachment.save()
            # insert pics in text
            if add_br:
                text += "<br/>"
            text += img_html.format(os.path.join(settings.MEDIA_URL,
                                                 attachment.file.name))
        # scraped posts are visible by default
        post = Post(title=title, text=text, pub_date=pubdate, is_visible=True)
        post.save()
        saved.append(post)
        # remove source data from data_dir
        for f in ['text'] + pics:
            os.remove(_get_path(f))
        os.rmdir(_get_path())
    return sorted(saved, key=lambda p: p.pub_date, reverse=True)
