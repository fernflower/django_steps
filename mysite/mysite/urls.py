import django.conf.urls as urls
from django.conf.urls import i18n

urlpatterns = i18n.i18n_patterns(
    '',
    urls.url(r'^', urls.include('posts.urls', namespace="posts")),)
