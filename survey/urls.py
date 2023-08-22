from django.urls import path
from . import views

app_name = 'survey'

urlpatterns = [
    path('services_survey/', views.services_survey, name='services_survey'),
    path('survey_thank_you/', views.thank_you, name='survey_thank_you'),

]
