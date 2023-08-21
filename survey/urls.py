from django.urls import path
from . import views

app_name = 'survey'

urlpatterns = [
    path('services_survey/', views.services_survey, name='home'),
    path('survey_thank_you/', views.survey_thank_you, name='survey_thank_you'),

]
