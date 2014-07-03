from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from contacts.forms import ContactForm
from contacts.models import Message


def process_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = Message()
            msg.sender_name = form.cleaned_data.get('name')
            msg.sender_email = form.cleaned_data.get('email')
            msg.text = form.cleaned_data.get('text')
            msg.phone = form.cleaned_data.get('phone')
            msg.pub_date = timezone.now()
            msg.save()
            # send message via email
            send_mail(subject="A message from {} ({})".\
                      format(msg.sender_name, msg.phone),
                      message=msg.text, from_email=msg.sender_email,
                      recipient_list=settings.EMAIL_RECIPIENT_LIST)
            return HttpResponseRedirect(reverse('contacts:message_sent'))
    else:
        form = ContactForm()
    return render(request, 'contacts/form.html', {'form': form})


def message_sent(request):
    return render(request, 'contacts/sent.html')
