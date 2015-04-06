from django.test import TestCase
from boots.elements import display_elements


class TestPageHeader(TestCase):


    def test_page_header(self):

        title ='This is the Title'
        sub = 'this is the sub'
        ph = display_elements.PageHeader(title, sub=sub)
        result = str(ph)
        needle = '<h1>{0} <small>{1}</small></h1>'.format(title, sub)
        self.assertInHTML(needle, result)
