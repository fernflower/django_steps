from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'contacts.views.process_message', name='show_form'),
                       url(r'^sent/$', 'contacts.views.message_sent', name='message_sent'))
