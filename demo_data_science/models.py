from django.db import models


class Order(models.Model):
    order_number = models.IntegerField(null=True)
    quantity_ordered = models.IntegerField(blank=True, null=True)
    price_each = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_line_number = models.IntegerField(blank=True, null=True)
    sales = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_date = models.CharField(max_length=50)
    status = models.CharField(max_length=255, blank=True, null=True)
    qtr_id = models.IntegerField(blank=True, null=True)
    month_id = models.IntegerField(blank=True, null=True)
    year_id = models.IntegerField(blank=True, null=True)
    product_line = models.CharField(max_length=255, blank=True, null=True)
    msrp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_code = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address_line1 = models.CharField(max_length=255, blank=True, null=True)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    territory = models.CharField(max_length=255, blank=True, null=True)
    contact_last_name = models.CharField(max_length=255, blank=True, null=True)
    contact_first_name = models.CharField(max_length=255, blank=True, null=True)
    deal_size = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Order #{self.order_number} - {self.customer_name}"
