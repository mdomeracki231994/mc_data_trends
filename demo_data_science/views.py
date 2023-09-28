from django.shortcuts import render
from .db import *


def index(request):
    world_sales = get_world_sales()
    world_sales_labels = world_sales[1]
    world_sales_data = world_sales[0]

    usa_product = get_usa_product_breakdown()
    usa_breakdown_labels = usa_product[0]
    usa_breakdown_data = usa_product[1]

    france_product = get_spain_product_breakdown()
    spain_breakdown_labels = france_product[0]
    spain_breakdown_data = france_product[1]

    france_product = get_france_product_breakdown()
    france_breakdown_labels = france_product[0]
    france_breakdown_data = france_product[1]

    context = {
        'world_sales_labels': world_sales_labels,
        'world_sales_data': world_sales_data,
        'usa_breakdown_labels': usa_breakdown_labels,
        'usa_breakdown_data': usa_breakdown_data,
        'spain_breakdown_labels': spain_breakdown_labels,
        'spain_breakdown_data': spain_breakdown_data,
        'france_breakdown_labels': france_breakdown_labels,
        'france_breakdown_data': france_breakdown_data,

    }

    return render(request, 'dashboard/index.html', context)
