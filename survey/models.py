from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.TextField()
    is_radio = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    def get_title(self):
        return self.question.text


class Response(models.Model):
    first_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    business = models.CharField(max_length=255)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)
    selected_choice = models.ManyToManyField(Choice)
