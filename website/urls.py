from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thankyou_page, name='thank-you'),

]
