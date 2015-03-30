from django import forms
from .widgets import (CalendarWidget,
                      DateRangeWidget,
                      RightSideAddOnWidget,
                      AtSymbolWidget,
                      DollarSignWidget,
                      DropDownWidget)


class DropDownField(forms.CharField):

    def __init__(self, dropdown, *args, **kwargs):
        self.widget = DropDownWidget(dropdown)
        super(DropDownField, self).__init__(*args, **kwargs)

class RightSideAddOnField(forms.CharField):
    '''A class that defines a custom widget for rendering a dollar
    sign input field'''

    widget = RightSideAddOnWidget

class DollarSignField(forms.IntegerField):
    '''A class that defines a custom widget for rendering a dollar
    sign input field'''

    widget = DollarSignWidget

class AtSymbolInputField(forms.CharField):

    widget = AtSymbolWidget

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


