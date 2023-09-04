from django.db import models


class SalesLead(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    company_name = models.CharField(max_length=100, null=True)
    website = models.URLField()
    company_address_line_1 = models.CharField(max_length=200, null=True)
    company_address_line_2 = models.CharField(max_length=200, null=True)
    company_city = models.CharField(max_length=200, null=True)
    company_state = models.CharField(max_length=200, null=True)
    company_zip = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    is_customer = models.BooleanField(default=False)
    customer_type = models.CharField(max_length=20, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    initial_email = models.DateTimeField(auto_now_add=True)
    date_last_contacted = models.DateTimeField(auto_now_add=True)
    source_of_lead = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True)
    lead_owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.company_name}"
