from django.conf.urls import url

import posts.views as p_views


urlpatterns = [
    url(r'^contact_me$', p_views.ContactFormView.as_view()),
    url(r'^get_videos', p_views.IndexView.get_videos_as_json),
    url(r'^$', p_views.IndexView.as_view())]
