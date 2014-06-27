from django.db import models


class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.CharField(max_length=100)
    message = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "Name:{subject}\nEmail:{sender}\n{msg}".\
            format(subject=self.sender_name, sender=self.sender_email,
                   msg=self.message)
