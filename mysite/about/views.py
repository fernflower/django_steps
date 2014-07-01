from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from about.models import Member


class AboutView(generic.ListView):
    template_name = "about/about.html"
