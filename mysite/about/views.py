from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from about.models import Member


class AboutView(generic.ListView):
    template_name = "about/about.html"
    model = Member
    context_object_name = 'members'


class GroupDataView(generic.TemplateView):
    template_name = "about/about_base.html"


class DetailMember(generic.DetailView):
    template_name = "about/member.html"
    model = Member
