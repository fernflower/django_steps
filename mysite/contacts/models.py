from django.db import models
from django.conf import settings


class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "Name:{subject}\nEmail:{sender}\n{msg}".\
            format(subject=self.sender_name, sender=self.sender_email,
                   msg=self.text)


class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, choices=zip(settings.CONTACT_TYPES,
                                                        settings.CONTACT_TYPES))

    def __str__(self):
        return "Name:{}\nEmail:{}\nPhone:{}\nWebsite:{}\n".format(
            self.name, self.email, self.phone, self.website)
