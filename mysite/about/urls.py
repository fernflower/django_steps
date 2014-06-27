from django.conf.urls import patterns, url
from about import views


urlpatterns = patterns('',
                       url(r'^$', views.ContactFormView.as_view(), name='contact_form'))
