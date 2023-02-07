# Задача: Длинномер.
# Дано: список строковых значений.
#
# Задание: написать функцию, которая возвращает список длин каждой строки.
#
# Пример:
#
#  ['Tina', 'Raj', 'Tom'], результат: [4, 3, 3]


# Using comprehension list
def to_get_length(input_list: list[str]) -> list[int]:
    return [len(word) for word in input_list]


# Using map function
def to_get_length_map(input_list: list[str]) -> list[int]:
    result = map(lambda word: len(word), input_list)
    return list(result)


if __name__ == "__main__":
    print(to_get_length(['Tina', 'Raj', 'Tom']))
