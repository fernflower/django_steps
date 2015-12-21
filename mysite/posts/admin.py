from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from posts.models import Post


class ComplexDeleteAdmin(admin.ModelAdmin):
    # FIXME has to be completely removed after Posts/Attachments connection
    # (it is of no use due to non-empty queryset restriction)
    actions = ['remove_all_items']

    def remove_all_items(self, request, queryset=None):
        self.model.objects.all().delete()
    remove_all_items.short_description = "Delete all items"


class PostAdmin(MarkdownModelAdmin):
    fieldsets = [(None, {'fields': ['title',  'is_visible', 'text']}),
                 ('Date information', {'fields': ['pub_date']}), ]
    list_display = ['title', 'is_visible', 'pub_date']


admin.site.register(Post, MarkdownModelAdmin)
