from django.db.models import Sum, Count
from .models import Order


def get_world_sales():
    world_sales_qs = Order.objects.values('country').annotate(total_sales=Sum('sales')).order_by('-total_sales')
    world_sales_labels = []
    world_sales_data = []
    for country in world_sales_qs:
        world_sales_labels.append(country['country'])
        world_sales_data.append(int(country['total_sales']))

    return world_sales_data, world_sales_labels


def get_usa_product_breakdown():
    usa_breakdown = Order.objects.filter(country='USA').values('product_line').annotate(
        product_line_count=Count('product_line')).order_by('product_line')
    usa_breakdown_labels = []
    usa_breakdown_data = []
    for sale_data in usa_breakdown:
        usa_breakdown_labels.append(sale_data['product_line'])
        usa_breakdown_data.append((sale_data['product_line_count']))
    return usa_breakdown_labels, usa_breakdown_data


def get_spain_product_breakdown():
    spain_breakdown = Order.objects.filter(country='Spain').values('product_line').annotate(
        product_line_count=Count('product_line')).order_by('product_line')
    spain_breakdown_labels = []
    spain_breakdown_data = []
    for sale_data in spain_breakdown:
        spain_breakdown_labels.append(sale_data['product_line'])
        spain_breakdown_data.append((sale_data['product_line_count']))
    return spain_breakdown_labels, spain_breakdown_data


def get_france_product_breakdown():
    france_breakdown = Order.objects.filter(country='France').values('product_line').annotate(
        product_line_count=Count('product_line')).order_by('product_line')
    france_breakdown_labels = []
    france_breakdown_data = []
    for sale_data in france_breakdown:
        france_breakdown_labels.append(sale_data['product_line'])
        france_breakdown_data.append((sale_data['product_line_count']))
    return france_breakdown_labels, france_breakdown_data

