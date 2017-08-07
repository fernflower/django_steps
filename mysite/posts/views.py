from django import http
from django.views import generic

import forms


class IndexView(generic.TemplateView):
    template_name = 'posts/index.html'
    send_to_list = ['inavasilevskaya@gmail.com']


class ContactFormView(generic.edit.FormView):
    form_class = forms.ContactForm

    def form_valid(self, form):
        form.send_email()
        return http.HttpResponse("Message sent!")
