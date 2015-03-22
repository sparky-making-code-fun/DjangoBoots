from django.shortcuts import render_to_response
from django.views.generic import View
from .forms import DemoForm

class DemoView(View):

    def get(self, request):
        '''Just a simple demo view for the widgets'''

        form = DemoForm()


        return render_to_response('boots/demo.html', {'form': form})

