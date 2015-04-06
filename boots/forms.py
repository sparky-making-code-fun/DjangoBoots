__author__ = 'sparky'
from django import forms
from .fields import fields as boot_fields

class DemoForm(forms.Form):

    date_range = boot_fields.DateRangeField()
    calendar = boot_fields.CalendarDateField()
    name = boot_fields.AtSymbolInputField('demofinchfoobarbaz')
    money = boot_fields.DollarSignField()
    data = {'actions': [{'href': 'http://google.com', 'label': 'Search Google'},
                        {'href': 'http://bing.com', 'label': 'Search Bing'}]}
    searchterm = boot_fields.DropDownField(data, max_length=30)






