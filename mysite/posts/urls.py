from django.conf import settings
from django.conf.urls import patterns, url
from posts import views


urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^favourites/$', views.FavouritePostsView.as_view(),
                           name='favourites'),
                       # /posts/1
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       # attachments /posts/attachment/1
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}))
