from django.conf.urls import url, patterns

import posts.views as p_views


urlpatterns = patterns(
    '',
    url(r'^contact_me$', p_views.ContactFormView.as_view()),
    url(r'^$', p_views.IndexView.as_view()))
