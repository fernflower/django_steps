from django.conf import settings
from django.views import generic
from django.utils import timezone
from django.core.mail import send_mail
from posts.views import GeneralContextMixin
from contacts.forms import ContactForm
from contacts.models import Message, ContactInfo


class ContactUsView(generic.edit.FormView, GeneralContextMixin):
    template_name = "contacts/form.html"
    success_url = "/contacts/sent/"
    form_class = ContactForm

    def form_valid(self, form):
            msg = Message()
            msg.sender_name = form.cleaned_data.get('name')
            msg.sender_email = form.cleaned_data.get('email')
            msg.text = form.cleaned_data.get('text')
            msg.phone = form.cleaned_data.get('phone')
            msg.pub_date = timezone.now()
            msg.save()
            # send message via email
            send_mail(subject="A message from {} ({})".
                      format(msg.sender_name, msg.phone),
                      message=msg.text, from_email=msg.sender_email,
                      recipient_list=settings.EMAIL_RECIPIENT_LIST)
            return super(ContactUsView, self).form_valid(form)


class MessageSentView(generic.TemplateView, GeneralContextMixin):
    template_name = "contacts/sent.html"


class ContactInfoView(generic.ListView):
    model = ContactInfo
    template_name = "contacts/contact_info.html"

    def get_context_data(self, **kwargs):
        context = super(ContactInfoView, self).get_context_data(**kwargs)
        context['contacts_main'] = ContactInfo.objects.filter(
            type='main').first()
        context['contacts_friends'] = ContactInfo.objects.filter(type='friends')
        return context
