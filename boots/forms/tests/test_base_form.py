__author__ = 'sparky'
from django import test
from boots.forms.boots_base_form import BootsBaseForm
from django import forms

class Foo(BootsBaseForm):
    number = forms.IntegerField()


class TestBootsBaseForm(test.TestCase):

    def test_as_ul(self):
        number = 'bubba'
        expected = """<div class="alert alert-danger" role="alert">
        <ul class="errorlist"><li>Enter a whole number.</li></ul></div>"""
        data = {"number": number}
        f = Foo(data)
        f.is_valid()
        result = f.as_ul()
        self.assertInHTML(expected, result)

    def test_as_p(self):
        number = 'bubba'
        expected = """<div class="alert alert-danger" role="alert">
        <ul class="errorlist"><li>Enter a whole number.</li></ul></div>"""
        data = {"number": number}
        f = Foo(data)
        f.is_valid()
        result = f.as_p()
        self.assertInHTML(expected, result)

    def test_as_table(self):
        number = 'bubba'
        expected = """<div class="alert alert-danger" role="alert">
        <ul class="errorlist"><li>Enter a whole number.</li></ul></div>"""
        # <tr><th><label for="id_number">Number:</label></th><td><ul class="errorlist"><li>Enter a whole number.</li></ul><input id="id_number" name="number" type="number" value="bubba" /></td></tr>
        data = {"number": number}
        f = Foo(data)
        f.is_valid()
        result = f.as_table()
        print result
        self.assertInHTML(expected, result)
