
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from .views import question_details, questions, results, raw_results

urlpatterns = [
    url(r'^$', questions, name='hello'),
    url(r'^questions/$', questions, name='questions'),
    url(r'^results/$', results, name='results'),
    url(r'^raw-results/$', raw_results, name='raw-results'),
    url(r'^questions/(?P<question_id>[0-9]+)/details/$', question_details, name='details')
]
