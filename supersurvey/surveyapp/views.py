# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect
from .models import Question, Answer, Session

from .forms import SurveyForm


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
    sum = 0
    for answer in answers:
        sum += int(answer.answer)
    return (sum / answers.count()) if answers.count() > 0 else 0


def distribution(question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=question)
    result = []
    for i, variant in enumerate(question.variants):
        count = answers.filter(answer=i).count()
        result.append({'answer': variant, 'number': count})
    return result


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
    sorted(result, key=lambda t: t[0])
    users_dict = {}
    for tup in result:
        if not tup[0] in users_dict:
            users_dict[tup[0]] = []
        questions_dict = {'title': tup[1].text, 'answer': tup[2].answer}
        users_dict[tup[0]].append(questions_dict)
    return HttpResponse(users_dict)
