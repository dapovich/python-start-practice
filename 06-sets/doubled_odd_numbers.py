# get the list of doubled odd numbers from [0, n)


def to_doubled_odd(size: int) -> list[int]:
    assert size != 0, "Error: can't get a sequence of doubled odd numbers in zero range."

    return [2 * number for number in range(size) if number % 2]


def main():
    answers = {
        1 : to_doubled_odd(5),
        2 : to_doubled_odd(7),
        3 : to_doubled_odd(8),
    }

    expected_answers = {
        1 : [2, 6],
        2 : [2, 6, 10],
        3 : [2, 6, 10, 14],
    }

    assert answers[1] == expected_answers[1], f"Your input: {answers[1]}\n expected: {expected_answers[1]}"
    assert answers[2] == expected_answers[2], f"Your input: {answers[2]}\n expected: {expected_answers[2]}"
    assert answers[3] == expected_answers[3], f"Your input: {answers[3]}\n expected: {expected_answers[3]}"

    print("TESTS PASSED")



if __name__ == '__main__':
    main()
