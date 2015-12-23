from django.conf import settings
from django.conf.urls import patterns, url
from posts import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^preview', views.preview, name='preview'),
    url(r'^(?P<pk>\d+)/update', views.update, name='update'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^about', views.about_author, name='about'),
    url(r'^delete/all', views.destroy, name='delete_all'),
    url(r'^delete', views.delete_multiple, name='delete_multiple'))
