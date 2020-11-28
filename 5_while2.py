"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"How are you?": "Fine, thanks!",
                         "What are you doing now?": "I am writing a code.",
                         "What programming language do you use?": "Python, of course.",
                         "Do you know other programming languages?": "Don't bother me. I'm busy."
                         }


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        question = input("Enter question: ")
        answer = answers_dict.get(question)
        if answer is None:
            break
        else:
            print(answer)


if __name__ == "__main__":
    ask_user(questions_and_answers)
