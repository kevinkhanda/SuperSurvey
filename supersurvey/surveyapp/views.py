# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response, redirect
from .models import Question

from .forms import SurveyForm


# Create your views here.
def index(request):
    return HttpResponse("Hi, folk! You are on a Super Survey index.")


def hello(request):
    return render(request, "hello.html", {'message': 'message from view'})

def save_answer(request, question, answer):
    pass

@csrf_exempt
def questions(request):
    extra_questions = Question.objects.filter(deleted=False)
    form = SurveyForm(request.POST or None, questions=extra_questions)
    if form.is_valid():
        for (question, answer) in form.answers():
            save_answer(request, question, answer)
        return redirect("hello")

    return render_to_response("survey.html", {'form': form})

def question_details(request, question_id):
    queried_question = Question.objects.filter(pk=question_id)
    return HttpResponse(queried_question)
