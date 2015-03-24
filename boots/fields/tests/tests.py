from django.test import TestCase
from boots.fields import widgets


class TestWidgets(TestCase):

    def test_calendar_widget_render(self):
        '''does our calendar widget have an ID?'''

        cal_wig = widgets.CalendarWidget()

        result = cal_wig.render('testname', '12-12-2015',
                                attrs={'id': 'testid'})
        needle = '<input type="text" date="12-12-2015"  id="testid"  name="testname"  >'
        self.assertInHTML(needle, result, 1)
