# Дано: координаты расставленных пешек в виде набора строк.
#
# Задание. Шахматы известны по всему миру, и практически всем людям знакомы их основные правила игры. 
# В игре используется набор фигур, которые могут ходить по игровому полю различными способами, что обеспечивает 
# огромное количество различных игровых комбинаций (к примеру, количество возможных шахматных партий оценивается Шенноном в 10^118). 
# В этой задаче мы будем исследовать правила игры пешками.
#
# Вам предоставляется набор координат, в которых расставлены белые пешки. Вы должны подсчитать количество защищенных пешек.


def to_determine_protected_pawns(input_coordinates: set) -> int:
    protected_pawns = 0
    for coordinate in input_coordinates:
        char = ord(coordinate[0])
        number = int(coordinate[1]) - 1
        expected_pawn_left = str(chr(char - 1) + str(number))
        expected_pawn_right = str(chr(char + 1) + str(number))
        if (expected_pawn_left in input_coordinates) or (expected_pawn_right in input_coordinates):
            protected_pawns += 1

    return protected_pawns


if __name__ == '__main__':

    test_input_1 = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}
    test_result_1 = to_determine_protected_pawns(test_input_1)
    print(f"Test 1:\nInput: {test_input_1}\nOutput: {test_result_1}", end='\n\n')
    assert test_result_1 == 1, print("Test 1: FAILED")


    test_input_2 = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
    test_result_2 = to_determine_protected_pawns(test_input_2)
    print(f"Test 2:\nInput: {test_input_2}\nOutput: {test_result_2}", end='\n\n')
    assert test_result_2 == 6, print("Test 2: FAILED")

    print("TESTS PASSED.")
