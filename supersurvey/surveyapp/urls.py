
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from .views import hello, question_details, questions, results

urlpatterns = [
    url(r'^hello/$', hello, name='hello'),
    url(r'^questions/$', questions, name='questions'),
    url(r'^results/$', results, name='results'),
    url(r'^questions/(?P<question_id>[0-9]+)/details/$', question_details, name='details')
]
