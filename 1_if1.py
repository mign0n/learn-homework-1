"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def determine_occupation(age):
    """
    This function is determines by age what the user should do:
    study in kindergarten, school, University, or work.

    :param age: the integer that represents age of a person
    :return: one element from ('study in kindergarten', 'study in school', 'study in University', 'work')
    """
    occupations = ('study in kindergarten', 'study in school', 'study in University', 'work')
    if 3 <= age <= 6:
        result = occupations[0]
    elif 7 <= age <= 16:
        result = occupations[1]
    elif 17 <= age <= 23:
        result = occupations[2]
    elif 24 <= age <= 65:
        result = occupations[3]
    return result


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('How old are you? Enter integer please. _'))
    occupation = determine_occupation(age)
    print(occupation)


if __name__ == "__main__":
    main()
