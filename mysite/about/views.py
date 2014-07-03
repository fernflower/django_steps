from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from about.models import Member


class AboutView(generic.ListView):
    template_name = "about/about.html"
    model = Member
    context_object_name = 'members'


class GroupDataView(RedirectView):
    def get_redirect_url(self):
        return reverse_lazy('about:member', kwargs={'pk': 5},
                             current_app='about')


class DetailMember(generic.DetailView):
    template_name = "about/member.html"
    model = Member
