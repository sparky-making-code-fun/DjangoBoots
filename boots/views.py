from django.shortcuts import render_to_response
from django.views.generic import View
from .forms import DemoForm
from .elements import display_elements

class DemoView(View):

    def get(self, request):
        '''Just a simple demo view for the widgets'''

        form = DemoForm()
        title = 'DjangoBoots Demo Page!'
        sub = 'Its a work in progress'
        page_header = display_elements.PageHeader(title, sub=sub)

        return render_to_response('boots/demo.html', {'form': form, 'pagehead': page_header})

