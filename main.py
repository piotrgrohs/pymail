import json
import datetime

sample_html_file = "/Users/piotr/Projects/github/pymail/sample/index.html"
html_file = "/Users/piotr/Projects/github/pymail/index.html"
json_file = "/Users/piotr/Projects/github/pymail/data.json"
# state output from json
passed = "passed"
failed = "failed"
inform = "problem"


def headershtml(d):
    return f'<th>{d}</th>'


def rowshtml(d):
    return f'<td>{d}</tr>'


def color_p(color, d):
    return f'<p style="color:{color}">{d}</p>'


def color_text(d):
    if d == passed:
        return color_p('green', d)
    elif d == failed:
        return color_p('red', d)
    elif d == inform:
        return color_p('orange', d)
    else:
        return color_p('black', d)


def header(data):
    return [headershtml(d) for d in data]


def jsontotable(_json):
    table_start = '<table>'
    table_end = '</table>'
    table = f'{table_start}'
    for key, value in _json.items():
        table += '<tr>'
        table += headershtml(key)
        new_var = value
        _value = color_text(new_var)
        table += rowshtml(_value)
        table += '</tr>'
    return table


def date():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def time():
    return datetime.datetime.now().strftime("%H:%M")


# open html file
f = open(sample_html_file, "r")
html = f.read()
f.close()

# open json file
f = open(json_file, "r")
_json = json.load(f)
f.close()

jsontotable = jsontotable(_json)

html = html.replace("{table}", jsontotable)
html = html.replace("{date}", date())
html = html.replace("{time}", time())

# save file html
f = open(html_file, "w")
f.write(html)
f.close()
