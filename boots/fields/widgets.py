__author__ = 'sparky'
from django import forms
from django.template.loader import render_to_string
from datetime import datetime
import os


class AtSymbolWidget(forms.TextInput):

    def render(self, name, value, attrs=None):
        data = {'name': name, 'value': value}
        if attrs is not None:
            data.update(attrs)
        template_path = '{0}/templates/boots'.format(os.path.dirname(
            os.path.realpath(__file__)))
        data = {'attrs': data}
        return render_to_string('at_input.html', data, dirs=[template_path])


class CalendarWidget(forms.DateInput):

    def render(self, name, value, attrs=None):
        '''Render a date widget as a bootstrap calendar'''

        if attrs is None:
            attrs = {'id': name, 'class': 'CalendarWidget'}

        data = {'name': name, 'date': value}
        attrs.update(data)
        data = {'attrs': attrs}
        template_path = '{0}/templates/boots'.format(os.path.dirname(
            os.path.realpath(__file__)))
        return render_to_string('calendar.html', data, dirs=[template_path])


class DateRangeWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets = (forms.DateInput(attrs={}),
                   forms.DateInput(attrs={}))
        if attrs is None:
            attrs = {'class': 'DateRangeWidget'}
        elif 'class' not in attrs.keys():
            attrs.update({'class': 'DateRangeWidget'})

        super(DateRangeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [datetime.strptime(value, '%d-%m-%Y'),datetime.strptime(value, '%d-%m-%Y')]
        return [None, None]

    def format_output(self, rendered_widgets):
        template_path = '{0}/templates/boots'.format(os.path.dirname(
            os.path.realpath(__file__)))
        data = {'min': rendered_widgets[0], 'max': rendered_widgets[1]}
        return render_to_string('date_range.html', data, dirs=[template_path])

