
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from .views import hello, question_details, questions, survey_results

urlpatterns = [
    url(r'^hello/$', hello, name='hello'),
    url(r'^questions/$', questions, name='questions'),
    url(r'^questions/(?P<question_id>[0-9]+)/details/$', question_details, name='details'),
    url(r'^questions/results$', survey_results, name='results')
]
