from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['total_sales', 'country']


class USAProductSoldSerializer(serializers.ModelSerializer):
    product_line_count = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ['country', 'product_line', 'product_line_count']


class USAMonthlySales(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
