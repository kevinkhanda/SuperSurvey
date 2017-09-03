# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect
from .models import Question, Answer, Session

from .forms import SurveyForm
from itertools import groupby


def save_answer(request, question, answer):
    session_id = Session.objects.all().get(pk=1).session_id
    Answer.objects.create(
        question=Question.objects.all().get(pk=question),
        session_id=session_id,
        answer=answer,
    ).save()


@csrf_exempt
def questions(request):
    # setting session for current user
    if request.method == 'POST':
        session = Session.objects.all().get(pk=1)
        session_id = session.session_id + 1
        session.session_id = session_id
        session.save()
    # loading questions
    extra_questions = Question.objects.filter(deleted=False)
    form = SurveyForm(request.POST or None, questions=extra_questions)
    if form.is_valid():
        for (question, answer) in form.answers():
            save_answer(request, question, answer)
        return redirect('hello')

    return render_to_response('survey.html', {'form': form})


def question_details(request, question_id):
    queried_question = Question.objects.filter(pk=question_id)
    return HttpResponse(queried_question)


def mean(question_id):
    answers = Answer.objects.filter(question=Question.objects.get(pk=question_id))
    answers_sum = 0
    for answer in answers:
        answers_sum += int(answer.answer)
    return (answers_sum / answers.count()) if answers.count() > 0 else 0


def distribution(question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=question)
    result = []
    for i, variant in enumerate(question.variants):
        count = answers.filter(answer=i).count()
        result.append({'answer': variant, 'number': count})
    return result

@login_required(login_url='/survey/login/')
def survey_statistics(request):
    questions_list = []
    all_questions = Question.objects.filter(deleted=False)
    for q in all_questions:
        question = {'type': q.type, 'title': q.text}
        if q.type == 'NR':
            question['value'] = mean(q.pk)
        elif q.type == 'MC':
            question['answers'] = distribution(q.pk)
        elif q.type == 'TE':
            answers = Answer.objects.filter(question=q)
            answers_list = []
            for answer in answers:
                answers_list.append(answer.answer)
            question['answers'] = answers_list
        else:
            print('Can not recognize question type %s' % q.type)
        questions_list.append(question)
    return render_to_response('statistics.html', {'questions': questions_list})

@login_required(login_url='/survey/login/')
def survey_answers(request):
    result = []
    questions_list = Question.objects.filter(deleted=False)
    for question in questions_list:
        answers = Answer.objects.filter(question=question)
        for answer in answers:
            result.append((
                answer.session_id,
                question,
                answer
            ))
    groups = []
    for k, g in groupby(result, lambda f: f[0]):
        groups.append(list(g))
    users_dict = {'users': []}
    for questions_group in groups:
        user = {'questions': []}
        for question in questions_group:
            user['questions'].append({'title': question[1].text, 'answer': question[2].answer})
        users_dict['users'].append(user)
    return render_to_response('answers.html', users_dict)
