__author__ = 'sparky'
from django import forms
from django.template.loader import render_to_string
from django.utils.html import format_html

class CalendarWidget(forms.DateInput):

    def __init
    def render(self, name, value, attrs=None):
        '''Render a date widget as a bootstrap calendar'''

        data = {'name': name, 'date': value}

        return render_to_string('widgets/calendar.html', data)


class DateRangeWidget(forms.MultiWidget):

    def __init__(self, widget, *args, **kwargs):
        widgets = (widget, widget)
        super(DateRangeWidget, self).__init__(widgets=widgets, *args, **kwargs)

    def decompress(self, value):
        return value

    def format_output(self, rendered_widgets):

        data = {'min': rendered_widgets[0], 'max': rendered_widgets[1]}
        return render_to_string('widgets/date_range.html', data)

