__author__ = 'sparky'
from django import forms
from .fields import fields as boot_fields


class DemoForm(forms.Form):
    """Just a simple form class to inspect our widgets"""

    date_range = boot_fields.DateRangeField()
    calendar = boot_fields.CalendarDateField()
    name = boot_fields.AtSymbolInputField('demofinchfoobarbaz')
    money = boot_fields.DollarSignField()
    data = dict(actions=[
        dict(href='http://google.com', label='Search Google'),
        dict(href='http://bing.com', label='Search Bing')])
    searchterm = boot_fields.DropDownField(data, max_length=30)
    radio = boot_fields.RadioField()
