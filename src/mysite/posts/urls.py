from django.conf.urls import patterns, url
from posts import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       # /posts/1
                       url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'))
