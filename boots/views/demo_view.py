# coding=utf-8
"""
This is really a throw away class We just need to view
what we are working on
"""


from boots.views.base import BootsFixedContainerView
from boots.elements import display_elements
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
from boots.forms import forms as boots_forms


class ErrorDemo(View):

    def get(self, request):

        form = boots_forms.ErrorExample()
        context = RequestContext(request)
        return render_to_response('boots/error.html',
                                  {'form': form},
                                  context)


    def post(self, request):
        form = boots_forms.ErrorExample(request.POST)
        print request.POST
        if not form.is_valid():
            context = RequestContext(request)
            return render_to_response('boots/error.html',
                                      {'form': form},
                                      context)




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
        form = boots_form.DemoForm()
        title = 'DjangoBoots Demo Page!'
        sub = 'Its a work in progress'
        page_header = display_elements.PageHeader(title, sub=sub)
        elements = {'elements': [page_header, form]}
        return self.render(elements)
