# coding=utf-8
"""
This is really a throw away class We just need to view
what we are working on
"""

from django.shortcuts import render_to_response
from boots.views.base import BootsFixedContainerView
from boots.forms import DemoForm
from boots.elements import display_elements


# noinspection PyUnusedLocal,PyUnresolvedReferences
class DemoView(BootsFixedContainerView):
    """Just looking at our widgets"""
    template_name = 'boots/demo.html'

    # noinspection PyMethodMayBeStatic
    def get(self, request, *args, **kwargs):
        """
        Just a simple demo view for the widgets
        :param request:
        """
        form = DemoForm()
        title = 'DjangoBoots Demo Page!'
        sub = 'Its a work in progress'
        page_header = display_elements.PageHeader(title, sub=sub)
        elements = {'elements': [page_header, form]}
        return self.render(elements)
