"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def spec_compare_strings(string1, string2):
    result = None
    if not (isinstance(string1, str) and isinstance(string2, str)):
        result = 0
    elif string1 == string2:
        result = 1
    elif len(string1) > len(string2):
        result = 2
    elif string2 == 'learn':
        result = 3
    return result


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    params1 = [1, 'Hello', 'Hi', 'Python']
    params2 = ['YAY', 2, 'Hi', 'learn']
    for string1 in params1:
        for string2 in params2:
            print(spec_compare_strings(string1, string2))


if __name__ == "__main__":
    main()
