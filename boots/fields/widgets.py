__author__ = 'sparky'
from django import forms
from django.template.loader import render_to_string
from django.utils.html import format_html
import os


class CalendarWidget(forms.DateInput):

    def render(self, name, value, attrs=None):
        '''Render a date widget as a bootstrap calendar'''

        if attrs is None:
            attrs = {'id': name}
        data = {'name': name, 'date': value}
        attrs.update(data)
        data = {'attrs': attrs}
        template_path = '{0}/templates/boots'.format(os.path.dirname(
            os.path.realpath(__file__)))
        return render_to_string('calendar.html', data, dirs=[template_path])


class DateRangeWidget(forms.MultiWidget):

    def __init__(self):
        widgets = (forms.DateInput(attrs={}),
                   forms.DateInput(attrs={}))
        super(DateRangeWidget, self).__init__(widgets=widgets)

    def decompress(self, value):
        return value

    def format_output(self, rendered_widgets):
        template_path = '{0}/templates/boots'.format(os.path.dirname(
            os.path.realpath(__file__)))
        data = {'min': rendered_widgets[0], 'max': rendered_widgets[1]}
        return render_to_string('date_range.html', data, dirs=[template_path])

