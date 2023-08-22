from django.shortcuts import render, redirect
from .models import Survey, Question, Response, PersonInfo


def services_survey(request):
    surveys = Survey.objects.all()

    if request.method == 'POST':
        survey_id = int(request.POST['survey_id'])
        survey = Survey.objects.get(pk=survey_id)
        questions = survey.question_set.all()

        person_info = PersonInfo(
            name=request.POST['name'],
            business_name=request.POST['business_name'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email'],
        )
        person_info.save()

        for question in questions:
            question_id = str(question.id)
            answer = request.POST.get('question_' + question_id)
            if answer:
                response = Response(
                    question=question,
                    person=person_info,
                )
                response.save()
                response.answers.create(answer=answer)

        return redirect('survey:survey_thank_you')

    context = {'surveys': surveys}
    return render(request, 'survey/services_survey.html', context)

def thank_you(request):
    return render(request, 'survey/thank-you-survey.html')
