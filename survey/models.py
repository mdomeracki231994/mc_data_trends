from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=100)


class PersonInfo(models.Model):
    name = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    person = models.ForeignKey(PersonInfo, on_delete=models.CASCADE)


class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
