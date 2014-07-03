from django.conf.urls import patterns, url
from about import views


urlpatterns = patterns('',
                       url(r'^group/$', views.AboutView.as_view(), name='group'), 
                       url(r'^(?P<pk>\d+)/$', views.DetailMember.as_view(), name='member'),
                       url(r'^$', views.GroupDataView.as_view(), name='index'))
