from jinja2 import Environment, FileSystemLoader
from jinja2 import FunctionLoader # (тоже что и filelouder, только загружает шаблон по ф-ии)

# *******************Загрузчик шаблонов
persons = [
    {'name':'Коля', 'old': 18, 'weight': 36},
{'name':'Оля', 'old': 58, 'weight': 39},
{'name':'Кля', 'old': 28, 'weight': 76},
]

file_loader = FileSystemLoader('for_jinja')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users = persons)
# print(msg)

# funclouder
def loadTpl(path):
    if path == 'index':
        return '''Имя {{ u.name }}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''

file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)

tm = env.get_template('index')
msg = tm.render(u = persons[0])
# print(msg


# ***************конструкции include и import
persons = [
    {'name':'Коля', 'old': 18, 'weight': 36},
{'name':'Оля', 'old': 58, 'weight': 39},
{'name':'Кля', 'old': 28, 'weight': 76},
]

file_loader = FileSystemLoader('for_jinja')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain='http://progs.com', title='Про Jinja')
# print(msg)



# ***************Наследование (расширение) шаблонов

file_loader = FileSystemLoader('for_jinja')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
output = tm.render()
print(output)