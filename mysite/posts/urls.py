from django.conf.urls import url, patterns

import posts.views as p_views


urlpatterns = patterns(
    '',
    url(r'^contact_me$', p_views.ContactFormView.as_view()),
    url(r'^get_videos', p_views.IndexView.get_videos_as_json),
    url(r'^$', p_views.IndexView.as_view()))
