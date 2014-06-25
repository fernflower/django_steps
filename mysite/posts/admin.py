from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from posts.models import Post


class PostAdmin(SummernoteModelAdmin):
    fieldsets = [ (None, {'fields': ['title', 'text']}),
                  ('Date information', {'fields': ['pub_date']}), ]

admin.site.register(Post, PostAdmin)
