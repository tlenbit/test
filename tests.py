import unittest
from collections import OrderedDict

from json_to_html import json_to_html

class TestJsonToHtmlConverter(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(json_to_html(OrderedDict()), '')

    def test_empty_list(self):
        self.assertEqual(json_to_html([]), '')

    def test_dict_root(self):
        json = OrderedDict([('h1', 'title')])
        self.assertEqual(json_to_html(json), '<h1>title</h1>')

    def test_list_root(self):
        json = []
        json.append(OrderedDict([('h1', 'title')]))
        result = '<ul><li><h1>title</h1></li></ul>'
        self.assertEqual(json_to_html(json), result)

    def test_nested_list(self):
        json = []
        json.append(OrderedDict([('div', [OrderedDict([('p', 'I am nested')]), OrderedDict([('span', 'So do I')])])]))
        result = '<ul><li><div><ul><li><p>I am nested</p></li><li><span>So do I</span></li></ul></div></li></ul>'
        self.assertEqual(json_to_html(json), result)

    def test_tag_classes(self):
        json = OrderedDict()
        json['div.class1.class2'] = 'smth'
        self.assertEqual(json_to_html(json), '<div class="class1 class2">smth</div>')

    def test_tag_ID(self):
        json = OrderedDict()
        json['div#id1'] = 'smth'
        self.assertEqual(json_to_html(json), '<div id="id1">smth</div>')

    def test_classes_and_IDs(self):
        json = OrderedDict()
        json['div.class1.class2#id1.class3'] = 'smth'
        self.assertEqual(json_to_html(json), '<div id="id1" class="class1 class2 class3">smth</div>')

    def test_HTML_chars_escaping(self):
        json = OrderedDict()
        json['div'] = '<a></a>'
        self.assertEqual(json_to_html(json), '<div>&lt;a&gt;&lt;/a&gt;</div>')

if __name__ == '__main__':
    unittest.main()
