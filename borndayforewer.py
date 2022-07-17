"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


def date_answers(name, date_in, date_true, flag='', min_date=-100000, max_date=100000):
    flag_result = True
    if flag == 'year':
        min_date, max_date = 0, 2022
    elif flag == 'month':
        min_date, max_date = 1, 12
    elif flag == 'day':
        min_date, max_date = 1, 31
    if date_in != date_true:
        if date_in < min_date or date_in > max_date:
            print('Ты ошибся. Такой даты  нет. Попробуй еще раз!')
        elif date_in < date_true:
            print(f'Ты ошибся. {name} родился позже. Попробуй еще раз!')
        else:
            print(f'Ты ошибся. {name} родился раньше. Попробуй еще раз!')
        flag_result = False
    return flag_result


def month_convert(answer_str_in):
    dict_month = {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
                  'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12}
    digital_month = 0
    answer_str = answer_str_in.lower()
    if answer_str in dict_month:
        digital_month = dict_month[answer_str]
    return digital_month


person = {'name': 'Пушкин',
          'year': 1799,
          'month': 6,
          'day': 6}

dict_questions = {'year': 'Ты знаешь в каком году родился он родился?\n',
                  'month': 'Правильно! А какой месяц рождения?\n',
                  'day': 'Правильно! А какого числа?\n'}

print(f'Привет, наш сегодняшний герой - {person["name"]}...')
for key in dict_questions:
    answer = input(f'{dict_questions[key]}')
    flag_answer = False
    while not flag_answer:
        if key == 'month':
            while month_convert(answer) == 0:
                answer = input('Такого названия месяца не существует. Повтори, пожалуйста:\n')
            answer = month_convert(answer)
        else:
            while not answer.isdigit():
                answer = input('Введи, пожалуйста, число:\n')
        if date_answers(person['name'], int(answer), person[key], key) is True:
            break
        answer = input()
print('Bерно')
