"""
Display elements from Bootstrap
"""
from django.template.loader import render_to_string
import os


class BaseDisplayElement(object):

    def render(self):
        pass


class PageHeader(BaseDisplayElement):
    """A PageHeader element as defined by bootstrap"""

    def __init__(self, title, sub=None, **kwargs):
        self.title = title
        self.sub = sub
        if 'template' in kwargs:
            self.template = kwargs['template']
        else:
            self.template = 'pageheader.html'

    def render(self):
        """Return a string of HTML suitable for rendering in a browser"""

        data = {'text': self.title, 'sub': self.sub}
        template_path = '{0}/templates/'.format(os.path.dirname(
            os.path.realpath(__file__)))
        return render_to_string(self.template, data, dirs=[template_path])

    def __str__(self):
        return self.render()