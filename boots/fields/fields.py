from django import forms
from .widgets import (CalendarWidget,
                      DateRangeWidget)

class CalendarDateField(forms.DateField):
    '''A class that defines a custom widget for rendering
        a calendar picker datefield'''
    widget = CalendarWidget

class DateRangeField(forms.MultiValueField):

    default_error_messages = {'invalid_start': u'Enter a valid start date.',
                              'invalid_end': u'Enter a valid end date.'}

    def __init__(self, *args, **kwargs):
        if not 'initial' in kwargs:
            kwargs['initial'] = ['', '']

        fields = [forms.DateField(label='Min Date'), forms.DateField(label='Max Date')]

        super(DateRangeField, self).__init__(fields=fields,
                                             widget=DateRangeWidget(),
                                             *args, **kwargs)

    def compress(self, data_list):

        if data_list:
            return data_list
        return None

class TestForm(forms.Form):

    date_range = DateRangeField()

