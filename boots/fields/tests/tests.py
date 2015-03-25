from django.test import TestCase
from boots.fields import widgets


class TestWidgets(TestCase):

    def test_calendar_widget_render(self):
        '''does our calendar widget have an ID?'''

        cal_widg = widgets.CalendarWidget()

        result = cal_widg.render('testname', '12-12-2015')
        needle = '<input type="text"  date="12-12-2015"  class="CalendarWidget"  name="testname"  >'
        self.assertInHTML(needle, result, 1)

    def test_date_range_widget(self):

        dr_widg = widgets.DateRangeWidget()
        result = dr_widg.render('testwidget', '12-12-2015')
        needle1 = '<input class="DateRangeWidget" name="testwidget_0" type="text" value="2015-12-12" />'
        needle2 = '<input class="DateRangeWidget" name="testwidget_1" type="text" value="2015-12-12" />'
        self.assertInHTML(needle1, result, count=1)
        self.assertInHTML(needle2, result, count=1)
