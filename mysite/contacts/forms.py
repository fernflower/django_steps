from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=14)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
    cc_myself = forms.BooleanField(required=False, widget=forms.HiddenInput())
