import json


def html_element(tag_name, inner_html):
    return f'<{tag_name}>{inner_html}</{tag_name}>'

def parse_dict(d):
    return ''.join([html_element(tag_name, d[tag_name]) for tag_name in d])

def json_to_html(source):
    return '<ul>' + ''.join([f'<li>{parse_dict(el)}</li>' for el in source]) + '</ul>'


if __name__ == '__main__':
    with open('source.json') as f:
        source = json.load(f)

    with open('index.html', 'w') as f:
        f.write(json_to_html(source))
