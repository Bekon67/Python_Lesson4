"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


def answers(answer, date, flag_date='year'):
    while answer != date:
        if flag_date == 'month' and answer != date:
            print('Ты ошибся. Попробуй еще раз!')
            answer = input()
        elif flag_date == 'day' and (answer < 1 or answer > 30):
            print('Ты ошибся.Такой даты в июне нет. Попробуй еще раз!')
            answer = int(input())
        elif answer < date:
            print('Ты ошибся. Пушкин родился позже. Попробуй еще раз!')
            answer = int(input())
        else:
            print('Ты ошибся. Пушкин родился раньше. Попробуй еще раз!')
            answer = int(input())


bornyear = 1799
bornmonth = 'июнь'
bornday = 6

answers(int(input('Привет, ты знаешь в каком году родился Пушкин?\n')), bornyear)
answers(input('Правильно! А какой месяц рождения? Введи прописью с маленькой буквы:\n'), bornmonth, 'month')
answers(int(input('Правильно! А какого числа?\n')), bornday, 'day')
print('Bерно')
