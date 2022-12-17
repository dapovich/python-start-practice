# 2. Палиндром.
# Дано: слово, состоящее только из строчных латинских букв.
#
# Задание: написать функцию, которая возвращает True, если слово палиндромом, иначе False.
#
# Палиндро́м — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 404; слова «топот» в русском языке; текст «а роза упала на лапу Азора» и пр.
#
# Примеры:
#
#  'lol', результат: True
#  'hi', результат: False


def is_polindrom(input_value: str) -> bool:
    stack = set()
    if input_value.isalpha():
        for char in input_value.lower().strip():
            if char not in stack:
                stack.add(char)
            else:
                stack.remove(char)
        if len(stack) <= 1:
            return True
    return False


if __name__ == '__main__':
    arguments = {
        1 : 'madam',
        2 : 'hello',
        3 : '',
        4 : 'level',
        5 : 'lovely',
        6 : 'Cinegenic',
        7 : 'noon',
    }

    tests = {
        1 : is_polindrom(arguments[1]),
        2 : is_polindrom(arguments[2]),
        3 : is_polindrom(arguments[3]),
        4 : is_polindrom(arguments[4]),
        5 : is_polindrom(arguments[5]),
        6 : is_polindrom(arguments[6]),
        7 : is_polindrom(arguments[7]),
    }

    expected_answers = {
        1 : True,
        2 : False,
        3 : False,
        4 : True,
        5 : False,
        6 : True,
        7 : True,
    }

    for i in range(1, len(tests) + 1):
        print(f"Test {i}:\nInput: {arguments[i]}\nOutput: {tests[i]}\nExpected output: {expected_answers[i]}", end='\n\n')
        assert tests[i] == expected_answers[i], print(f"Test {i}: FAILED")
    print("TESTS PASSED :)")
