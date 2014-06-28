from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import admin
from contacts.models import Message

# TODO have to find a way to disable Editing
class MessageAdmin(admin.ModelAdmin):
    change_form_template = "contacts/admin_edit.html"
    def save_model(self, request, obj, form, change):
        pass

admin.site.register(Message, MessageAdmin)
