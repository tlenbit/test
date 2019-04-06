import json


def html_element(tag_name, inner_html):
    return f"<{tag_name}>{inner_html}</{tag_name}>"

def parse_dict(d):
    return html_element('h1', d['title']) + html_element('p', d['body'])

def json_to_html(source):
    return ''.join([parse_dict(el) for el in source])


if __name__ == '__main__':
    with open('source.json') as f:
        source = json.load(f)

    with open('index.html', 'w') as f:
        f.write(json_to_html(source))

