from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, AttachmentAdmin
from django_summernote.models import Attachment
from posts.models import Post


class ComplexDeleteAdmin(admin.ModelAdmin):
    actions = ['remove_all_items']

    def remove_all_items(self, request, queryset=None):
        self.model.objects.all().delete()
    remove_all_items.short_description = "Delete all items"


class PostAdmin(SummernoteModelAdmin, ComplexDeleteAdmin):
    fieldsets = [(None, {'fields': ['title', 'is_favourite', 'is_visible',
                                    'text']}),
                 ('Date information', {'fields': ['pub_date']}), ]
    list_display = ['title', 'is_favourite', 'is_visible', 'pub_date']


class MyAttachmentAdmin(AttachmentAdmin, ComplexDeleteAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.unregister(Attachment)
admin.site.register(Attachment, MyAttachmentAdmin)
