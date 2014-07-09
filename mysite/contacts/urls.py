from django.conf.urls import patterns, url
from contacts.views import ContactInfoView, ContactUsView


urlpatterns = patterns('',
                       url(r'^$', ContactUsView.as_view(), name='show_form'),
                       url(r'^get-contacts/$', ContactInfoView.as_view(), name='get_contacts'),
                       url(r'^sent/$', 'contacts.views.message_sent', name='message_sent'))
