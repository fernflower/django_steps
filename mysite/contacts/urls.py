from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'contacts.views.process_message', name='show_form'),
                       url(r'^send/$', 'contacts.views.send_message', name='send'))
