import django.conf.urls as urls
from django.contrib import admin

admin.autodiscover()

urlpatterns = urls.patterns(
    '',
    urls.url(r'^', urls.include('posts.urls', namespace="posts")),
    urls.url(r'^admin/', urls.include(admin.site.urls)),)
