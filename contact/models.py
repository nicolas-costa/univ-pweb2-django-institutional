from django.db import models

# Create your models here.


class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    msg = models.TextField(max_length=4000)