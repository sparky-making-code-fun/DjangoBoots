# coding=utf-8
"""
Tests for page element classes
"""
import django.test
from boots.elements import display_elements


class TestPageHeader(django.test.TestCase):
    def test_page_header(self):
        title = 'This is the Title'
        sub = 'this is the sub'
        ph = display_elements.PageHeader(title, sub=sub)
        result = str(ph)
        needle = '<h1>{0} <small>{1}</small></h1>'.format(title, sub)
        self.assertInHTML(needle, result)


class TestPanel(django.test.TestCase):

    def test_panel(self):
        class FooPanel(display_elements.Panel):
            title = 'Foo Panel'
            title_size = 2

        p = FooPanel()

        ph = display_elements.PageHeader('header', sub='subber')
        p.add(ph)

        result = str(p)
        needle = '<h2>Foo Panel</h2>'
        self.assertInHTML(needle, result)
        needle = '<h1>header <small>subber</small></h1>'
        self.assertInHTML(needle, result)


class TestNaviation(django.test.TestCase):

    def test_add(self):

        nav = display_elements.Navigation()

        nav.add('label1', '/url1')
        nav.add('label2', '/url2', rank=0)
        nav.add('label3', '/url3')
        nav.add('label4', '/url4', rank=0)

        self.assertEqual(len(nav.urls), 4)
        self.assertEqual(nav.urls[0], ('label4', '/url4',))
        self.assertEqual(nav.urls[1], ('label2', '/url2',))
        self.assertEqual(nav.urls[2], ('label1', '/url1',))
        self.assertEqual(nav.urls[3], ('label3', '/url3',))

