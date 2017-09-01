from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hi, folk! You are on a Super Survey index.")


def hello(request):
    return render(request, "hello.html", {'message': 'message from view'})


def questions(request):
    response = "Here is the list of questions"
    return HttpResponse(response)


def question_details(request, question_id):
    response = "You are looking at details of question %s."
    return HttpResponse(response % question_id)
