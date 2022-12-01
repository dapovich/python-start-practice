# get the list of doubled odd numbers from [0, n)


def to_doubled_odd(size: int) -> list[int]:
    assert size >= 0, f"Argument size must be equal or greater than 0, but you got {size=}"
    return [2 * number for number in range(size) if number % 2]


def main():

    sizes = {
        1 : 5,
        2 : 7,
        3 : 8,
        4 : 1,
        5 : 0
    }

    answers = {
        1 : to_doubled_odd(sizes[1]),
        2 : to_doubled_odd(sizes[2]),
        3 : to_doubled_odd(sizes[3]),
        4 : to_doubled_odd(sizes[4]),
        5 : to_doubled_odd(sizes[5]),
    }

    expected_answers = {
        1 : [2, 6],
        2 : [2, 6, 10],
        3 : [2, 6, 10, 14],
        4 : [],
        5 : [],
    }

    for i in range(1, len(answers) + 1):
        assert answers[i] == expected_answers[i], f"Your input: {answers[i]}\n Expected: {expected_answers[i]}"
        print(f"Size of sequence: n = {sizes[i]}")
        print(f"Your output: {answers[i]}")
        print(f"Expected output: {expected_answers[i]}", end='\n\n')

    print("TESTS PASSED :)")


if __name__ == '__main__':
    main()
