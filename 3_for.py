from random import randint

"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def create_scores():
    """
    This function is creates list of dictionaries with random scores of different classes students.
    :return: list of dicts as example: [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
    """
    class_letters = [x for x in 'абвгде']
    class_digits = [str(x) for x in range(1, 12)]
    school_scores = []
    for letter in class_letters:
        for digit in class_digits:
            school_scores.append(
                {'school_class': ''.join((digit, letter)),
                 'scores': [randint(1, 5) for x in range(randint(5, 15))]
                 })
    return school_scores


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores = create_scores()
    school_scores_number = 0
    school_scores_sum = 0

    for class_scores in school_scores:
        class_scores_number = len(class_scores['scores'])
        class_scores_sum = sum(class_scores['scores'])
        school_scores_number += class_scores_number
        school_scores_sum += class_scores_sum
        class_average_score = class_scores_sum / class_scores_number
        print(f"Average score of {class_scores['school_class']} grade: {class_average_score}")

    school_average_score = school_scores_sum / school_scores_number
    print(f"Average school score: {school_average_score}")


if __name__ == "__main__":
    main()
