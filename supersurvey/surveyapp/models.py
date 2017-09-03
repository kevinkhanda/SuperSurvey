from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
CHOICE_TYPE = (
    ('MC', 'Multiple Choice'),
    ('NR', 'Numerical Response'),
    ('TE', 'Text Entry'),
)


class Session(models.Model):
    session_id = models.IntegerField(default=0)


class Question(models.Model):
    text = models.TextField()
    variants = ArrayField(models.CharField(max_length=256))
    type = models.CharField(max_length=2, choices=CHOICE_TYPE)
    number = models.IntegerField()
    deleted = models.BooleanField(default=False)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    session_id = models.IntegerField()
    answer = models.TextField()
