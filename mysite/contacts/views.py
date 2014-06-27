from django.utils import timezone
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from contacts.forms import ContactForm
from contacts.models import Message


def process_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = Message()
            msg.sender_name = form.cleaned_data.get('name')
            msg.sender_email = form.cleaned_data.get('email')
            msg.message = form.cleaned_data.get('message')
            msg.pub_date = timezone.now()
            msg.save()
            return HttpResponseRedirect(reverse('contacts:send'))
    else:
        form = ContactForm()
    return render(request, 'contacts/form.html', {'form': form})


def send_message(request):
    # TODO
    return HttpResponseRedirect(reverse('posts:index'))
