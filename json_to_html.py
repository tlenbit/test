import json
import re
from collections import OrderedDict


def get_element(tag, inner_html, id='', classes=[]):
    id_part = f' id="{id}"' if id else ''
    classes_part = f' class="{" ".join(classes)}"' if classes else ''
    return f'<{tag}{id_part}{classes_part}>{inner_html}</{tag}>'

def parse_key(key):
    ''' Parse key of the form: "p.my-class1#my-id.my-class2" '''
    if '#' in key:
        part1, part2, *_ = key.split('#')
        if _:
            raise Exception('Error: more than one id has been provided')
        tag, *classes1 = part1.split('.')
        id, *classes2 = part2.split('.')
        return {'tag': tag, 'id': id, 'classes': classes1 + classes2}

    if '.' in key:
        tag, *classes = key.split('.')
        return {'tag': tag, 'id': '', 'classes': classes}

    return {'tag': key, 'id': '', 'classes': []}

def json_to_html(source):
    if type(source) == str:
        return source

    if type(source) == OrderedDict:
        return ''.join([get_element(**parse_key(key), inner_html=json_to_html(source[key])) for key in source])

    if type(source) == list:
        return get_element('ul', ''.join([get_element('li', json_to_html(el)) for el in source]))


if __name__ == '__main__':
    with open('source.json') as f:
        raw_data = f.read().replace('\n', '')
        source = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(raw_data)

    with open('index.html', 'w') as f:
        f.write(json_to_html(source))
