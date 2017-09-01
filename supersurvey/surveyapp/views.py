from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


# Create your views here.
def index(request):
    return HttpResponse("Hi, folk! You are on a Super Survey index.")


def hello(request):
    return render(request, "hello.html", {'message': 'message from view'})


def questions(request):
    questions_list = Question.objects.filter(deleted=False)
    return HttpResponse(questions_list)


def question_details(request, question_id):
    queried_question = Question.objects.filter(pk=question_id)
    return HttpResponse(queried_question)
