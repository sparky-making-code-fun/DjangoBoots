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
from boots.forms import demo_form as boots_forms


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
class DemoView(View):
    """Just looking at our widgets"""
    template_name = 'boots/demo.html'

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        """
        Just a simple demo view for the widgets
        :param request:
        """
        form = boots_forms.DemoForm()
        title = 'DjangoBoots Demo Page!'
        sub = 'Its a work in progress'
        page_header = display_elements.PageHeader(title, sub=sub)
        elements = {'elements': [page_header, form]}
        return render_to_response(self.template_name, {'elements': [form, page_header]})

class PanelView(BootsFixedContainerView):

    template_name = "boots/paneldemo.html"

    def get(self, request, *args, **kwargs):

        my_panel = display_elements.Panel()
        my_panel.title = 'Happy Panels 1'
        my_panel.panel_type = 'primary'

        panel_2 = display_elements.Panel()
        panel_2.title = 'Happy Panels 2'
        panel_2.panel_type = 'warning'
        panel_2.footer ='We Gots Footers!'
        form = boots_forms.DemoForm()
        title = 'DjangoBoots Panel Demo!'
        sub = "Isn't Paneling great?"
        page_header = display_elements.PageHeader(title, sub=sub)
        my_panel.add(form)
        panel_2.add(form)
        elements = {'panels': [my_panel, panel_2], 'elements':[page_header]}
        return self.render(elements)

