# 2. Ленивое объединение
# Дано: 2 списка произвольной длины.
#
# Задание: написать функцию, которая возвращает результат объединения этих списков. Используйте функцию itertools.chain.
#
# Пример:
#
#  list(f([1, 2], [3, 4])), результат: [1, 2, 3, 4]


from itertools import chain


def to_combine(a: list, b: list) -> list:
    return list(chain(a, b))


if __name__ == "__main__":
    print(to_combine([1, 2], [3, 4]))
