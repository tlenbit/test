import json
from collections import OrderedDict

def get_element(tag, inner_html):
    return f'<{tag}>{inner_html}</{tag}>'

def json_to_html(source):
    if type(source) == str:
        return source
    if type(source) == OrderedDict:
        return ''.join([get_element(tag, json_to_html(source[tag])) for tag in source])
    if type(source) == list:
        return get_element('ul', ''.join([get_element('li', json_to_html(el)) for el in source]))


if __name__ == '__main__':
    with open('source.json') as f:
        raw_data = f.read().replace('\n', '')
        source = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(raw_data)

    with open('index.html', 'w') as f:
        f.write(json_to_html(source))
