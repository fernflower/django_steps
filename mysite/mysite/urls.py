import django.conf.urls as urls
from django.contrib import admin
from django.views.generic import TemplateView
import settings

admin.autodiscover()

urlpatterns = urls.patterns(
    '',
    urls.url(r'^posts/', urls.include('posts.urls', namespace="posts")),
    urls.url(r'^admin/', urls.include(admin.site.urls)),)
