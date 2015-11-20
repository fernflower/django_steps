# -*- coding: utf-8 -*-
import os
import requests
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

    html = "<html><body>%(msg)s</body></html>"

    try:
        scraped = SCRAPER.scrape_wall(count=count, offset=offset)
        posts = _load_scraped(scraped)
        return render_to_response('posts/show_scraped.html',
                                  {'posts': posts},
                                  context_instance=RequestContext(request))
    except subprocess.CalledProcessError as e:
        return http.HttpResponseBadRequest(html % {"msg": e.message})


def _load_scraped(posts):
    """Load scraped scraper.Post as models.Post.

    Data_dir param shows where to search for attachments.

    Posts are saved with is_visible=False and won't be visible to non-admins.
    After post has been saved into db data is removed from data_dir.
    """
    img_html = "<img src='%s' />"
    text_html = "<p>%s</p>"

    saved = []
    for post in posts:
        # post dir name has format postid_pubdate
        pubdate = timezone.make_aware(
            timezone.datetime.utcfromtimestamp(post.date), timezone.utc)
        title = u"Новость № %s" % post.id
        text = text_html % post.text
        for i, pic in enumerate(post.pics):
            add_br = False if i < 2 else True
            # upload attachments
            temp = 'tempfile.jpg'
            pic_data = requests.get(pic['url']).content
            with open(temp, 'wb') as f:
                f.write(pic_data)
            with open(temp, 'rb') as f:
                attachment = Attachment(name=pic['name'], file=File(f))
                attachment.save()
            os.remove(temp)
            # insert pics in text
            if add_br:
                text += "<br/>"
            text += img_html % (os.path.join(settings.MEDIA_URL,
                                             attachment.file.name))
        # scraped posts are invisible by default. Will be made visible after
        # changes are applied
        post = Post(title=title, text=text, pub_date=pubdate, is_visible=False)
        post.save()
        saved.append(post)
    return sorted(saved, key=lambda p: p.pub_date, reverse=True)
