from airium import from_html_to_airium

with open('index2.html', 'rt', encoding='UTF8') as f:
    html_str = f.readlines()

html_str = ''.join(html_str)
py_str = from_html_to_airium(html_str)

with open('build_index2.py', 'wt', encoding='UTF8') as f:
    f.write(py_str)
