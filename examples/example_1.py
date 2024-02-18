from stf.transformers import get_transformer


class T:
    pass


t = T()
json_data = '{"text": "Hello World!"}'
transformer = get_transformer(json_data, output=t)
transformer.transform({'hello_world': {'action': 'extract', 'filter': 'text'}})
print(t.hello_world)
"""
Hello World!
"""

transformer = get_transformer(json_data, output='json')
print(transformer.extract('text'))
"""
"Hello World!"
"""
print(transformer.transform({'hello_world': {'action': 'extract', 'filter': 'text'}}))
"""
{"hello_world": "Hello World!"}
"""

transformer = get_transformer(json_data, output='xml')
print(transformer.extract('text'))
"""
b'<?xml version="1.0" encoding="UTF-8" ?><root><item type="str">Hello World!</item></root>'
"""
print(transformer.transform({'hello_world': {'action': 'extract', 'filter': 'text'}}))
"""
b'<?xml version="1.0" encoding="UTF-8" ?><root><hello_world type="str">Hello World!</hello_world></root>'
"""

transformer = get_transformer(json_data, output='yaml')
print(transformer.extract('text'))
"""
Hello World!
...
"""
print(transformer.transform({'hello_world': {'action': 'extract', 'filter': 'text'}}))
"""
hello_world: Hello World!
"""


from django.template import Template
template = Template("<html><body>{{ hello_world }}</body></html>")
transformer = get_transformer(json_data, output=template)
print(transformer.transform({'hello_world': {'action': 'extract', 'filter': 'text'}}))
"""
<html><body>Hello World!</body></html>
"""