from django.template import Template, Context

__author__ = 'sparky'
from django.test import TestCase


class TestGridTag(TestCase):

    FLOW_TEMPLATE = Template({'{% load bootstrap_grids %} {% flow_grid %}'})
    TEMPLATE = Template({'{% load bootstrap_grids %} {% grid %}'})

    def test_flow_grid(self):

        rendered = self.FLOW_TEMPLATE.render(Context({}))
        needle= '<div class="content-flow">'
        self.assertIn(needle, rendered)

    def test_grid(self):

        rendered = self.TEMPLATE.render(Context({}))

        needle= '<div class="content">'
        self.assertIn(needle, rendered)
