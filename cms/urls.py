from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add_sales_leads/', views.add_sales_leads, name='add_sales_leads'),
    path('sales_leads/', views.sales_lead_index, name='sales_leads'),
]