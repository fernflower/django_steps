import django.conf.urls as urls
from django.conf.urls import i18n
from django.contrib import admin

admin.autodiscover()

urlpatterns = i18n.i18n_patterns(
    '',
    urls.url(r'^', urls.include('posts.urls', namespace="posts")),
    urls.url(r'^admin/', urls.include(admin.site.urls)),)
