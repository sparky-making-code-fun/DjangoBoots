__author__ = 'sparky'
from django import forms
from .fields import fields as boot_fields

class DemoForm(forms.Form):

    date_range = boot_fields.DateRangeField()
    calendar = boot_fields.CalendarDateField()
    name = boot_fields.AtSymbolInputField()
    money = boot_fields.DollarSignField()





