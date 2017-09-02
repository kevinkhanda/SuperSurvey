# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from operator import attrgetter


class SurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = sorted(list(kwargs.pop('questions')), key=attrgetter("number"))
        super(SurveyForm, self).__init__(*args, **kwargs)

        for i, question in enumerate(questions):
            if question.type == 'MC':
                vrs = question.variants
                self.fields['question_%s' % question.id] = forms.ChoiceField(
                    label=question.text,
                    choices=[(j, vrs[j]) for j in range(len(vrs))],
                    widget=forms.RadioSelect,
                    required=True)
            elif question.type == 'NR':
                self.fields['question_%s' % question.id] = forms.ChoiceField(
                    choices=[(i, i) for i in range(0, 11)],
                    label=question.text)
            elif question.type == 'TE':
                self.fields['question_%s' % question.id] = forms.CharField(
                    max_length=512,
                    required=True,
                    widget=forms.TextInput(),
                    label=question.text)

    def clean(self):
        cleaned_data = super(SurveyForm, self).clean()
        return cleaned_data

    def answers(self):
        for name, value in self.cleaned_data.items():
            if name.startswith('question_'):
                yield (int(name.split('_')[1]), value)
