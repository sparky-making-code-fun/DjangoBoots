# coding=utf-8
"""
First test written just to make sure it works
"""
from django.test import TestCase


class FakeTest(TestCase):

    def test_fake(self):
        self.assertEqual(1, 1)
