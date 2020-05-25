from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=512)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,unique=True)
    answer_text = models.CharField(max_length=128,blank=False)
