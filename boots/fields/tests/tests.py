from django.test import TestCase
from boots.fields import widgets
from boots.fields import fields as boot_fields


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

    def test_right_side_add_on(self):

        widge = widgets.RightSideAddOnWidget()
        expected = "anystringyouwant"
        result = widge.render('bubba', '@home', attrs={"add_on_text": expected})
        self.assertIn(expected, result)


    def test_dropdown_widget(self):

        dd_widg = widgets.DropDownWidget(dropdown={'actions':[{'href': 'http://www.google.com',
                                                               'label': 'Google Thing'},
                                                              {'href': 'http://fark.com',
                                                               'label': 'Fark Thing'}
                                                             ]}, attrs={'id': 'testid'})
        result = dd_widg.render('fake_name', 'fake_value', attrs=dd_widg.attrs)
        needle = '<li><a href="http://fark.com">Fark Thing</a></li>'
        self.assertInHTML(needle, result)

class TestFields(TestCase):

    def test_dropdown_field(self):
        data = {'actions':[{'href': 'http://www.google.com', 'label': 'Google Thing'},
                           {'href': 'http://fark.com', 'label': 'Fark Thing'}
                           ]
                }
        ddf = boot_fields.DropDownField(data, max_length=2)
        needle = '<li><a href="http://fark.com">Fark Thing</a></li>'
        result = ddf.widget.render('tstname', 'testvalue', attrs={'id':'testid'})
        self.assertInHTML(needle, result)

    def test_change_at_symbol_field(self):
        expected = "somestring"
        f = boot_fields.AtSymbolInputField(expected, symbol='!')
        result = f.widget.render("name", "value")
        needle = """<span class="input-group-addon" id="basic-addon2">!{0}</span>""".format(expected)
        self.assertInHTML(needle, result)

    def test_at_symbol_field(self):
        expected = "somestring"
        f = boot_fields.AtSymbolInputField(expected)
        result = f.widget.render("name", "value")
        needle = """<span class="input-group-addon" id="basic-addon2">@{0}</span>""".format(expected)
        self.assertInHTML(needle, result)