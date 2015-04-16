# coding=utf-8
"""
Display elements from Bootstrap
"""
from django.template.loader import render_to_string
from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import mark_safe
import os


class BaseDisplayElement(object):
    """
    A base class for display elements
    """
    def render(self):
        """
        This method should be implemented on child classes not here
        """
        pass


@python_2_unicode_compatible
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
        return mark_safe(render_to_string(self.template, data, dirs=[template_path]))
    def __str__(self):
        return self.render()


@python_2_unicode_compatible
class Panel(BaseDisplayElement):

    title = None
    title_size = 3
    contents = None
    template = None

    def add(self, element):
        if self.contents is None:
            self.contents = [element]
        else:
            self.contents.append(element)

    def render(self):

        data = {'title': self.title, 'title_size': self.title_size,
                'contents': self.contents}
        if self.template is None:
            template_path = '{0}/templates/'.format(os.path.dirname(
                os.path.realpath(__file__)))
            self.template = 'panel.html'

        return mark_safe(render_to_string(self.template, data, dirs=[template_path]))

    def __str__(self):
        return self.render()
