from django.conf.urls import patterns, url
from posts import views


urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       # /posts/1
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'))
