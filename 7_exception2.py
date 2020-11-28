"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""


def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    result = None
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except ValueError:
        print('Invalid argument value. Could not convert.')
    except TypeError:
        print('Invalid argument type. Must be string.')
    try:
        if max_discount > 99:
            raise ValueError('Max discount is too much.')
        if discount >= max_discount:
            result = price
        else:
            result = price - (price * discount / 100)
    except TypeError:
        print('Unsupported operand type for division. Must be int or float.')

    return result


if __name__ == "__main__":
    print(1, discounted(100, 2))
    print(2, discounted(100, "3"))
    print(3, discounted("100", "4.5"))
    print(4, discounted("five", 5))
    print(5, discounted("сто", "десять"))
    print(6, discounted(100.0, 5, "10"))
    print(7, discounted(100.0, 5, "3.5"))
