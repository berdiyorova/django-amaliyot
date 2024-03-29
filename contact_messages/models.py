from ckeditor.fields import RichTextField
from django.db import models



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    message_text = RichTextField()
    sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
