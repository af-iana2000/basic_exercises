# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = []
for student in students:
    names.append(student['first_name'])
print(Counter(names))


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = []
for student in students:
    names.append(student['first_name'])
max_name = max(Counter(names), key = Counter(names).get)
print(f'Самое частое имя среди учеников: {max_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
group_num = 0
for group in school_students:
    group_num += 1
    names = []
    for student in group:
        names.append(student['first_name'])
    max_name = max(Counter(names), key = Counter(names).get)
    print(f'Самое частое имя в классе {group_num}: {max_name}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_class in school:
    class_name = school_class['class']
    f_num = 0
    m_num = 0
    students = school_class['students']
    for student in students:
        if is_male.get(student['first_name']) == False:
            f_num += 1
        else:
            m_num += 1
    print(f'Класс {class_name}: девочки {f_num}, мальчики {m_num}')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
for school_class in school:
    class_name = school_class['class']
    f_num = 0
    m_num = 0
    students = school_class['students']
    for student in students:
        if is_male.get(student['first_name']) == False:
            f_num += 1
        else:
            m_num += 1
    school_class['male'] = m_num
    school_class['female'] = f_num
print(f'Больше всего мальчиков в классе {max(school, key = lambda x: x['male'])['class']}')
print(f'Больше всего девочек в классе {max(school, key = lambda x: x['female'])['class']}')