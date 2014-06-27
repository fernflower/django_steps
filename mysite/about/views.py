from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


class ContactFormView(generic.TemplateView):
    template_name = "about/form.html"
