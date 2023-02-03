# Дано: позиционный аргумент, как итерируемое или два или более позиционных аргументов. Необязательный ключевой аргумент, как функция.
# Задание.
# Роботы решили покопаться в себе и может быть даже улучшить что-нибудь. В этой задаче Вам нужно написать свою реализацию встроенных функций (версии для py3) min и max. Некоторые встроенные функции заблокированы здесь: import, eval, exec, globals. Не забудьте, что в этой задаче вам нужно реализовать две функции, а не одну как обычно.
# max(iterable, [, key]) or min(iterable, [, key]) max(arg1, arg2, args[, key]) or min(arg1, arg2, args[, key])
# Возвращает наибольший (наименьший) элемент в итерируемом (iterable) или наибольшее (наименьшее) из двух и более аргументов.
# Если дан только один позиционный аргумент, то он должен быть итерируемым. В этом случае функция возвращает наибольший (наименьший) элемент из данного итерируемого. Если даны два или более позиционных аргумента, то возвращен будет наибольший (наименьший) из данных аргументов.
# Необязательный ключевой аргумент key определяет функцию одного аргумента, которая используется для извлечения ключа для сравнения из каждого элемента массива (для примера, key=str.lower).
# Если массив содержит несколько максимальных (минимальных) значений, то функция возвращает первый по порядку в массиве.
# -- Python документация (Встроенные функции)
#
# Примеры:
#
# max(3, 2) == 3
#
# min(3, 2) == 2
#
# max([1, 2, 0, 3, 4]) == 4
#
# min("hello") == "e"
#
# max(2.2, 5.6, 5.9, key=int) == 5.6
#
# min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]


def max(*iterable, key=None):
    if len(iterable) == 0:
        raise TypeError('max expected at least one argument')
    if len(iterable) == 1:
        # Use tuple to prevent situation when there is one not iterable argument
        iterable = tuple(iterable[0])
    largest = iterable[0]
    if key is None:
        for elem in iterable:
            if elem > largest:
                largest = elem
        return largest
    else:
        largest_key = key(iterable[0])
        for elem in iterable:
            elem_key = key(elem)
            if elem_key > largest_key:
                largest = elem
                largest_key = elem_key
        return largest


def min(*iterable, key=None):
    if len(iterable) == 0:
        raise TypeError('max expected at least one argument')
    if len(iterable) == 1:
        iterable = tuple(iterable[0])
    smallest = iterable[0]
    if key is None:
        for elem in iterable:
            if elem < smallest:
                smallest = elem
        return smallest
    else:
        smallest_key = key(iterable[0])
        for elem in iterable:
            elem_key = key(elem)
            if elem_key < smallest_key:
                smallest = elem
                smallest_key = elem_key
        return smallest


if __name__ == '__main__':
    result_1 = max(3, 2)
    result_2 = min(3, 2)
    result_3 = max([1, 2, 0, 3, 4])
    result_4 = min("hello")
    result_5 = max(2.2, 5.6, 5.9, key=int)
    result_6 = min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1])
    result_7 = max([[1, 5], [2, 5], [9, 0]], key=lambda x: x[1])

    print(f"Test 1:\nInput: max(3, 2)\nOutput: {result_1}\nExpected output: 3")
    assert result_1 == 3,   print("Test 1: FAILED")
    print("Test 1: PASSED", end='\n\n')

    print(f"Test 2:\nInput: min(3, 2)\nOutput: {result_2}\nExpected output: 2")
    assert result_2 == 2,   print("Test 2: FAILED")
    print("Test 2: PASSED", end='\n\n')

    print(f"Test 3:\nInput: max([1, 2, 0, 3, 4])\nOutput: {result_3}\nExpected output: 4")
    assert result_3 == 4,   print("Test 3: FAILED")
    print("Test 3: PASSED", end='\n\n')

    print(f"Test 4:\nInput: min('hello')\nOutput: {result_4}\nExpected output: 'e'")
    assert result_4 == "e", print("Test 4: FAILED")
    print("Test 4: PASSED", end='\n\n')

    print(f"Test 5:\nInput: max(2.2, 5.6, 5.9, key=int)\nOutput: {result_5}\nExpected output: 5.6")
    assert result_5 == 5.6, print("Test 5: FAILED")
    print("Test 5: PASSED", end='\n\n')

    print(f"Test 6:\nInput: min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1])\nOutput: {result_6}\nExpected output: [9, 0]")
    assert result_6 == [9, 0], print("Test 6: FAILED")
    print("Test 6: PASSED", end='\n\n')

    print(f"Test 7:\nInput: max([[1, 5], [2, 5], [9, 0]], key=lambda x: x[0])\nOutput: {result_7}\nExpected output: [1, 5]")
    assert result_7 == [1, 5], print("Test 7: FAILED")
    print("Test 7: PASSED", end='\n\n')
