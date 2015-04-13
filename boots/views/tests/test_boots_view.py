__author__ = 'sparky'
from django.test import TestCase, RequestFactory
from boots.views.base import BootsView


class TestBootsView(TestCase):


    def test_render(self):
        request = RequestFactory().get('/home/')
        bv = BootsView(request=request)
        bv.container_type = 'test-container'
        bv.template_name = 'boots/test.html'
        result = bv.render({'test_content': 'Hello Test'})
        result.render()
        needle = '<div class="test-container">   Hello Test   </div>'
        self.assertInHTML(needle, result.rendered_content)
