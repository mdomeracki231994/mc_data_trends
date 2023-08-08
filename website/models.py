from django.db import models


class ContactInfo(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    message = models.TextField()
