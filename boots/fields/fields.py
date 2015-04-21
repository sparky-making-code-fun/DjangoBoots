# coding=utf-8
"""
Basic Bootstrap Field definitions
"""
from django import forms
from .widgets import (CalendarWidget,
                      DateRangeWidget,
                      RightSideAddOnWidget,
                      SymbolWidget,
                      DollarSignWidget,
                      DropDownWidget,
                      RadioWidget)


class RadioField(forms.ChoiceField):
    def __init__(self, radio, *args, **kwargs):
        self.widget = RadioWidget(radio)
        super(RadioField, self).__init__(*args, **kwargs)


class DropDownField(forms.CharField):
    """A simple drop down field widget"""

    def __init__(self, dropdown, *args, **kwargs):
        self.widget = DropDownWidget(dropdown)
        super(DropDownField, self).__init__(*args, **kwargs)


class RightSideAddOnField(forms.CharField):
    """A class that defines a custom widget for rendering a dollar
    sign input field"""

    widget = RightSideAddOnWidget


class DollarSignField(forms.IntegerField):
    """
    A class that defines a custom widget for rendering a dollar
    sign input field
    """

    widget = DollarSignWidget


class AtSymbolInputField(forms.CharField):
    """

    :param text:
    :param symbol:
    :param args:
    :param kwargs:
    """

    def __init__(self, text, symbol="@", *args, **kwargs):
        super(AtSymbolInputField, self).__init__(*args, **kwargs)
        self.widget = SymbolWidget(text, symbol=symbol)


class CalendarDateField(forms.DateField):
    """
    A class that defines a custom widget for rendering
    a calendar picker date field
    """

    widget = CalendarWidget


class DateRangeField(forms.MultiValueField):
    """

    :param args:
    :param kwargs:
    """
    default_error_messages = {'invalid_start': u'Enter a valid start date.',
                              'invalid_end': u'Enter a valid end date.'}

    def __init__(self, *args, **kwargs):
        if 'initial' not in kwargs:
            kwargs['initial'] = ['', '']

        fields = [forms.DateField(label='Min Date'),
                  forms.DateField(label='Max Date')]

        # noinspection PyArgumentList
        super(DateRangeField, self).__init__(fields=fields,
                                             widget=DateRangeWidget(),
                                             *args, **kwargs)

    def compress(self, data_list):

        """

        :param data_list:
        :return:
        """
        if data_list:
            return data_list
        return None
