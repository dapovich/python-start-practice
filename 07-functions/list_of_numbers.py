# 1. Список из числа.
# Дано: натуральное число N.
#
# Задание: написать функцию, которая возвращает список всех цифр этого числа в обратном порядке.
#
# Пример:
#
#  123, результат: [3, 2, 1]
#


def to_reverse(input_number: int) -> list[int]:
    if (input_number <= 0):
        return []
    reversed_numbers_list = []
    while input_number:
        digit = input_number % 10
        input_number //= 10
        reversed_numbers_list.append(digit)
    return reversed_numbers_list


if __name__ == '__main__':
    test_1 = to_reverse(123)
    test_2 = to_reverse(4985)
    test_3 = to_reverse(489)
    test_4 = to_reverse(1)

    expected_answer_1 = [3, 2, 1]
    expected_answer_2 = [5, 8, 9, 4]
    expected_answer_3 = [9, 8, 4]
    expected_answer_4 = [1]

    print(f"Test1:\nYour output: {test_1}\nExpected output: {expected_answer_1}", end='\n\n')
    assert test_1 == expected_answer_1, print("Test 1: FAILED")
    print(f"Test2:\nYour output: {test_2}\nExpected output: {expected_answer_2}", end='\n\n')
    assert test_2 == expected_answer_2, print("Test 2: FAILED")
    print(f"Test3:\nYour output: {test_3}\nExpected output: {expected_answer_3}", end='\n\n')
    assert test_3 == expected_answer_3, print("Test 3: FAILED")
    print(f"Test4:\nYour output: {test_4}\nExpected output: {expected_answer_4}", end='\n\n')
    assert test_4 == expected_answer_4, print("Test 4: FAILED")

    print("TESTS PASSED :)")
