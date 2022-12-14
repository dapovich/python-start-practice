# [Junior+] 5. Возраст привидений
# Дано: степень прозрачности, как целое число.
#
# Задание. У Николы появилось свободное время и он решил заняться исследованием привидений. Он хочет найти способ, как определять возраст привидений. Согласно древним фолиантам, возраст связан со степенью прозрачности призраков. Никола составил шкалу измерений прозрачности от 10000 до 0, где 10000 - это совсем не прозрачное "новорождённое" привидение (0 лет) и 0 - это уже невидимка (возраст неизвестен).
#
# После множества экспериментов, Никола кажется начел взаимосвязь. На каждый "день рождения", степень прозрачности привидения уменьшается на количество единиц, равное его возрасту, если возраст есть одно из чисел Фибоначчи (подробней здесь), иначе увеличивается на единицу.
#
# Для примера: "Новорождённое" привидение -- 10000 единиц прозрачности.
#
# 1 год -- 10000 - 1 = 9999 (1 число Фибоначчи).
#
# 2 года -- 9999 - 2 = 9997 (2 число Фибоначчи).
#
# 3 года -- 9997 - 3 = 9994 (3 число Фибоначчи).
#
# 4 года -- 9994 + 1 = 9995 (4 не число Фибоначчи).
#
# 5 лет -- 9995 - 5 = 9990 (5 число Фибоначчи). Помогите Николе написать функцию, которая будет определять возраст привидения по прозрачности. Вам известно измерение прозрачности, как число от 0 до 10000 включительно. Привидения не бывают старше 5000 лет, так как потом просто исчезают (серьезно, научный факт).
#
# Пример:
#
# прозрачность = 10000, возраст: 0
# прозрачность = 9999, возраст: 1
# прозрачность = 9997, возраст: 2
# прозрачность = 9994, возраст: 3
# прозрачность = 9995, возраст: 4
# прозрачность = 9990, возраст: 5


def check_age(opacity: int) -> int:
    temp_ghost_age = 10000

    # Use sets to make search in its for O(1)
    fibonacci_numbers = set()

    # Take in [0, 20) because 19-th fibonacci number is 4181
    # 20-th fibonacci number is 6765 that greater than 5000 (max ghost age)
    for idx in range(20):
        fibonacci_numbers.add(fibonacci_sequence(idx))

    for i in range(5000):
        if i in fibonacci_numbers:
            temp_ghost_age -= i
        else:
            temp_ghost_age += 1
        if temp_ghost_age == opacity:
            return i
    return 0


# Use recursive function to calculate n-th fibonacci_number
def fibonacci_sequence(n: int):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


if __name__ == '__main__':
    assert check_age(10000) == 0, print("TEST 1: FAILED")
    assert check_age(9999) == 1, print("TEST 2: FAILED")
    assert check_age(9997) == 2, print("TEST 3: FAILED")
    assert check_age(9994) == 3, print("TEST 4: FAILED")
    assert check_age(9995) == 4, print("TEST 5: FAILED")
    assert check_age(9990) == 5, print("TEST 6: FAILED") 

    print("TESTS PASSED :)")

