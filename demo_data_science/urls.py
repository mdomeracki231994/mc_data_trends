from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('total_country_sales/', views.OrderListView.as_view()),
    # path('product_line/', views.USAProductsSold.as_view()),
    # path('usa_monthly_sales/', views.USAMonthlySales.as_view()),
]
