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

    def __init__(self, field_klass, *args, **kwargs):
        if not 'initial' in kwargs:
            kwargs['initial'] = ['', '']

        fields = [field_klass(), field_klass()]

        super(DateRangeField, self).__init__(fields=fields,
                                             widget=DateRangeWidget(forms.TextInput),
                                             *args, **kwargs)


