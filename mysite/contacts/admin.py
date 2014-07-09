from django.contrib import admin
from contacts.models import Message, ContactInfo


class MessageAdmin(admin.ModelAdmin):
    change_form_template = "contacts/admin_edit.html"

    def save_model(self, request, obj, form, change):
        pass

admin.site.register(Message, MessageAdmin)
admin.site.register(ContactInfo)
