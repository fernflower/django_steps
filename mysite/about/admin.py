from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from about.models import Member


class MemberAdmin(SummernoteModelAdmin):
    fieldsets = [ ('Personal info', {'fields': ['name', 'birthday']}),
                  ('None', {'fields': ['info']}), ]

admin.site.register(Member, MemberAdmin)
