# coding=utf-8
"""
A demo form so we can easily show off and test
"""
__author__ = 'sparky'
from django.conf import settings
from django import forms
from boots.forms.boots_base_form import BootsBaseForm
from boots.fields import fields as boot_fields


class ErrorExample(BootsBaseForm):

    number = forms.IntegerField()
    ipaddress = forms.IPAddressField()
    name = forms.CharField(max_length=30)
    email = forms.EmailField()

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
    forms.Form
