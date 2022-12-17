# Дано: шифровальная решетка (4 на 4) и зашифрованный пароль (4 на 4) представлены, как массив строк.
#
# Задание. Помогите Софи написать дешифратор для паролей, которые Никола зашифровал с помощью шифровальной решетки. Шифрорешетка - это квадрат 4 на 4 с четырьмя вырезанными окошками. Поместите решетку на листе бумаги такого же размера с буквами, выписываете первые 4 символа, которые видно в окошках (см. рисунок). Затем поверните решетку на 90 градусов по часовой стрелке. Выпишите следующие символы и повторите поворот. В итоге процедура повторяется 4 раза. Таким образом сложно узнать пароль без специальной решетки.
#
# Напишите программу, которая поможет проводить данную процедуру.
#
# Пример:
#
#  (('X...',
#    '..X.',
#    'X..X',
#    '....'),
#   ('itdf',
#    'gdce',
#    'aton',
#    'qrdi'), результат: 'icantforgetiddqd'
#
#  (('....',
#    'X..X',
#    '.X..',
#    '...X'),
#   ('xhwc',
#    'rsqx',
#    'xqzz',
#    'fyzr')), результат: 'rxqrwsfzxqxzhczy'


def decoder(encryption_grid: tuple, encrypted_password: tuple) -> str:
    result = ""
    for _ in range(4):
        for substring_code, substring_password in zip(encryption_grid, encrypted_password):
            for char_code, char_password in zip(substring_code, substring_password):
                if char_code == 'X':
                    result += char_password
        # Specify strict=True option to ensure what we use zip with the iterables of equal length
        # Use the * operator in conjuction with zip() to unzip
        print(encryption_grid)
        encryption_grid = tuple(zip(*encryption_grid[::-1], strict=True))
        print(encryption_grid)
    return result
                    

if __name__ == '__main__':
    encryption_grid_test_1 = (('X...',
                               '..X.',
                               'X..X',
                               '....'));

    encrypted_password_test_1 = (('itdf',
                                  'gdce',
                                  'aton',
                                  'qrdi'));

    encryption_grid_test_2 = (('....',
                               'X..X',
                               '.X..',
                               '...X'))
    
    encrypted_password_test_2 = (('xhwc',
                                  'rsqx',
                                  'xqzz',
                                  'fyzr'))
    
    result_test_1 = decoder(encryption_grid_test_1, encrypted_password_test_1)
    expected_result_test_1 = 'icantforgetiddqd'
    result_test_2 = decoder(encryption_grid_test_2, encrypted_password_test_2)
    expected_result_test_2 = 'rxqrwsfzxqxzhczy'

    print(f"Your result: {result_test_1}")
    print(f"Expected result: {expected_result_test_1}", end='\n\n')

    print(f"Your result: {result_test_2}")
    print(f"Expected result: {expected_result_test_2}", end='\n\n')

    assert expected_result_test_1 == result_test_1, print("Test 1: FAILED")
    assert expected_result_test_2 == result_test_2, print("Test 2: FAILED")

    print("TESTS PASSED :)")

