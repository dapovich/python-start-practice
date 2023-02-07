# Задача Градусник.
# Дано: список градусов Цельсия.
#
# Задание: написать функцию, которая преобразовывает исходный список градусов Цельсия в список градусов Фаренгейта (https://ru.wikipedia.org/wiki/%D0%93%D1%80%D0%B0%D0%B4%D1%83%D1%81_%D0%A4%D0%B0%D1%80%D0%B5%D0%BD%D0%B3%D0%B5%D0%B9%D1%82%D0%B0).
#
# Пример:
#
#  [39.2, 36.5, 37.3, 37.8], результат: 
#  [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]


# Comprehension list
def to_fahrenheit(input_list: list) -> list:
    return [9/5 * value + 32 for value in input_list]


# Using map function
def to_fahrenheit_map(input_list: list) -> list:
    result = map(lambda value: 9/5 * value + 32, input_list)
    return list(result)


if __name__ == '__main__':
    print(to_fahrenheit_map([39.2, 36.5, 37.3, 37.8]))
