from django import forms
from django.conf import settings
from django.core import mail


class ContactForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    message = forms.CharField()
    email = forms.CharField()

    def send_email(self):
        msg = self.cleaned_data.get('message')
        from_email = self.cleaned_data.get('email')
        subject = ("A message from %(email)s AKA %(name)s (%(phone)s)" %
                   {"name": self.cleaned_data.get('name'),
                    "phone": self.cleaned_data.get('phone'),
                    "email": from_email})
        mail.send_mail(subject, msg, from_email, settings.EMAIL_RECIPIENT_LIST)
