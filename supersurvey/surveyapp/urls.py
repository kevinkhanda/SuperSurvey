
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import question_details, questions, survey_statistics, survey_answers

urlpatterns = [
    url(r'^$', questions, name='hello'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^questions/$', questions, name='questions'),
    url(r'^statistics/$', survey_statistics, name='statistics'),
    url(r'^answers/$', survey_answers, name='answers'),
    url(r'^questions/(?P<question_id>[0-9]+)/details/$', question_details, name='details')
]
