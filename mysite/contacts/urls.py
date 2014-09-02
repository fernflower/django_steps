from django.conf.urls import patterns, url
from contacts.views import ContactInfoView, ContactUsView, MessageSentView


urlpatterns = patterns('',
                       url(r'^$', ContactUsView.as_view(), name='show_form'),
                       url(r'^get-contacts/$', ContactInfoView.as_view(), name='get_contacts'),
                       url(r'^sent/$', MessageSentView.as_view(), name='message_sent'))
