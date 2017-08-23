from django.conf import settings
from django.conf.urls import url, patterns

import posts.views as p_views


def get_videos(filename=settings.VIDEOS_FILE):
    with open(filename, 'r') as f:
        # fields are url/name/date/id
        res = []
        for line in [l.strip() for l in f.readlines() if l.strip() != ""]:
            fields = line.split('|')
            if len(fields) > 0:
                video_id = fields[0].split('/')[-1]
                fields = [video_id] + fields
                res.append(fields)
        return res


urlpatterns = patterns(
    '',
    url(r'^contact_me$', p_views.ContactFormView.as_view()),
    url(r'^$', p_views.IndexView.as_view(), {'videos': get_videos()}))
