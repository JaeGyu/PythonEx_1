from jinja2 import Template


template = Template('''
Hello {{ name }}!
Sum : {{num | sum}}

{% if num is defined %}
    value of num: {{ num }}
    <ul>
        {% for item in num %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
{% else %}
    num is not defined
{% endif %}

{% if num[2] is divisibleby 3 %}
    num[2] is divisible by 3
{% else %}
    num[2] is not divisible by 3
{% endif %}
''')

print(template.render(name = 'John Doe', num = [1,2,3]))