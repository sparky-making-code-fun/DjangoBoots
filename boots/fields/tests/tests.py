from django.test import TestCase
from boots.fields import widgets


class TestWidgets(TestCase):

    def test_calendar_widget_render(self):
        '''does our calendar widget have an ID?'''

        cal_widg = widgets.CalendarWidget()

        result = cal_widg.render('testname', '12-12-2015',
                                attrs={'id': 'testid'})
        needle = '<input type="text" date="12-12-2015"  id="testid"  name="testname"  >'
        self.assertInHTML(needle, result, 1)

    def test_date_range_widget(self):

        dr_widg = widgets.DateRangeWidget(attrs={'id': 'testid', 'value': '12-12-2015'})
        result = dr_widg.render('testwidget', '12-12-2015')
        print result
