from jinja2 import Template, escape  # скоро escape устареет (markup.escape)

# name = 'Fudor'

#
# tm = Template('Hi {{ name }}')
# msg = tm.render(name=name)
# print(msg)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

per = Person('Лева', 20)

tm = Template('Мне {{ p.age }} и меня зовут {{ p.name }}')
msg = tm.render(p = per)

# print(msg)


# Экранирование, блоки row, for, if

data = '''{% raw %}Модуль Jinja вместо
оапределения {{ name }}
подставляетт соответствующее значение{% endraw %}'''

tm = Template(data)
msg = tm.render(name = 'Федор')

# print(msg)
#
# link = '''В HTML-документе ссылки определяются как
# <a href="#">Ссылка</a>'''
#
# msg = escape(link)

# print(msg)


# Блок for (с if такая же конструкция)
cities  = [
    {'id':1, 'city': 'Москва'},
{'id':3, 'city': 'Томск'},
{'id':5, 'city': 'Омск'},
{'id':7, 'city': 'Обь'},
]

link = '''<select name="cities">
{% for i in cities %}
    <option value="{{i['id']}}">{{i['city']}}</option>
{% endfor %}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)
# print(msg)







# ***************Фильтры
# Фильр sum и др.

cars = [
    {'model': 'audi', 'price': 23000},
{'model': 'mers', 'price': 90000},
{'model': 'bmw', 'price': 8000},
{'model': 'opel', 'price': 78000},
]

tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs = cars)
# print(msg)




# ***********макросы
# macro(вроде нужен, чтобы не повторять код)
html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value | e}}" size="{{ size }}">
{% endmacro -%}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
'''
tm = Template(html)
msg = tm.render()
# print(msg)

# call ******************пробел знаний***********урок 3  jinja на канале selfedu
# persons = [
#     {'name':'Коля', 'old': 18, 'weight': 36},
# {'name':'Оля', 'old': 58, 'weight': 39},
# {'name':'Кля', 'old': 28, 'weight': 76},
# ]
#
# html = '''
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for i in list_users -%}
#     <li>{{i.name}} {{caller(i)}}
# {%- endfor %}
# </ul>
# {%- endmacro %}
#
# {%call(user) list_users(users)%}
#     <ul>
#     <li>age: {{user.old}}
#     <li>weight: {{user.weight}}
#     </ul>
# {% endcall -%}
#
# {{list_users(users)}}  #&????????????????????????????????
# '''
#

# tm = Template(html)
# msg = tm.render(users = persons)
# print(msg)



