from django.conf.urls import patterns, include, url
from django.contrib import admin
from posts.sitemap import PostSitemapXML
from about.sitemap import MemberSitemapXML

admin.autodiscover()

sitemaps = {'posts': PostSitemapXML,
            'members': MemberSitemapXML}

urlpatterns = patterns('',
                       url(r'^about/', include('about.urls', namespace="about")),
                       url(r'^contacts/', include('contacts.urls', namespace="contacts")),
                       url(r'^posts/', include('posts.urls', namespace="posts")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^captcha/', include('captcha.urls')),
                       url(r'^summernote/', include('django_summernote.urls')),
                       (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
                        {'sitemaps': sitemaps}),)
