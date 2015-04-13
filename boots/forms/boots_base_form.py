__author__ = 'sparky'
from django import forms


class BootsBaseForm(forms.Form):

    def as_table(self):
        return self._html_output(
            normal_row='<tr%(html_class_attr)s><th>%(label)s</th><td>%(field)s%(help_text)s</td></tr>',
            error_row='<tr><td colspan="2" class="alert alert-danger" role="alert">%s</td></tr>',
            row_ender='</td></tr>',
            help_text_html='<br /><span class="helptext">%s</span>',
            errors_on_separate_row=True)

    def as_p(self):
        return self._html_output(
            normal_row='<p%(html_class_attr)s>%(label)s %(field)s%(help_text)s</p>',
            error_row='<div class="alert alert-danger" role="alert">%s</div>',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)

    def as_ul(self):
        return self._html_output(
            normal_row='<li%(html_class_attr)s>%(label)s%(field)s%(help_text)s</li>',
            error_row=' <li style="list-style-type: none;" class="alert alert-danger" role="alert">%s</li>',
            row_ender='</li>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)