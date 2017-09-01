from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^questions/(?P<question_id>[0-9]+)/details/$', views.question_details, name='details')
]
