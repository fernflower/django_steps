from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import admin
from contacts.models import Message

# TODO have to find a way to disable Editing
class MessageAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super(MessageAdmin, self).__init__(*args, **kwargs)
        #self.list_display_links = (None, )


admin.site.register(Message, MessageAdmin)
