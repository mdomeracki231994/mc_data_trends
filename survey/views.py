from django.shortcuts import render, redirect
from .models import *


def services_survey(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        business_name = request.POST.get('business_name')
        for question in Question.objects.all():
            selected_choice_id = request.POST.get(f'question_{question.id}')
            selected_choice = Choice.objects.get(pk=selected_choice_id)
            response = Response(
                first_name=name,
                email=email,
                phone_number=phone,
                business=business_name,
                survey=question.survey,
                question=question,
                selected_choice=selected_choice
            )
            response.save()
            return redirect('survey:survey_thank_you')

    survey = Survey.objects.all().first()
    questions = Question.objects.filter(survey=survey)
    context = {
        'survey': survey,
        'questions': questions,
    }
    return render(request, 'survey/services_survey.html', context)


def survey_thank_you(request):
    return render(request, 'survey/thank-you-survey.html')
