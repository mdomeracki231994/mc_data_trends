from django.db import models


class Client(models.Model):
    business_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    contacted_at = models.DateField(null=True, blank=True)
    converted_client = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Client Business: {self.business_name}, Client Name: {self.name}'
