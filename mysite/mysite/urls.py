from django.conf.urls import patterns, include, url
from django.contrib import admin
from posts.sitemap import PostSitemapXML

admin.autodiscover()

sitemaps = {'posts': PostSitemapXML}

urlpatterns = patterns(
    '',
    url(r'^posts/', include('posts.urls', namespace="posts")),
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include('django_markdown.urls')),
    url(r'^adminfiles/', include('adminfiles.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
     {'sitemaps': sitemaps}),)
