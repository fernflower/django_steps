from django.conf import settings
from django.conf.urls import patterns, url

import posts.views as p_views


def get_videos(filename=settings.VIDEOS_FILE):
    with open(filename, 'r') as f:
        return [l for l in f.readlines() if l.strip() != ""]


urlpatterns = patterns(
    '',
    url(r'^contact_me$', p_views.ContactFormView.as_view()),
    url(r'^$', p_views.IndexView.as_view(), {'videos': get_videos()}))
