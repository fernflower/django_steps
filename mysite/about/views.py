from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from contact_form.views import ContactFormView


class AboutView(generic.TemplateView):
    template_name = "about/about.html"

