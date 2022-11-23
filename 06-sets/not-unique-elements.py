# Find and return a new array of not unique elements in the input list


def find_non_unique(elements: list[int]) -> list[int]:
    return [element for element in elements if elements.count(element) > 1]


def main():

    testing_lists = {
        1 : [1, 2, 3, 1, 3],
        2 : [1, 2, 3, 4, 5],
        3 : [5, 5, 5, 5, 5],
        4 : [10, 9, 10, 10, 9, 8]
    }

    expected_answer = {
        1 : [1, 3, 1, 3],
        2 : [],
        3 : [5, 5, 5, 5, 5],
        4 : [10, 9, 10, 10, 9],
    }

    answers = {
        1 : find_non_unique(testing_lists[1]),
        2 : find_non_unique(testing_lists[2]),
        3 : find_non_unique(testing_lists[3]),
        4 : find_non_unique(testing_lists[4])
    }

    for i in range(1, len(testing_lists) + 1):
        assert answers[i] == expected_answer[i], f"Answer is wrong\n Your result: {answers[i]}\n expected: {expected_answer[i]}"
        print(f"Test {i}:")
        print(f"Input list:", testing_lists[i])
        print(f"Output list:", answers[i])
        print(f"Expected list:", expected_answer[i], end=2*'\n')

    print("Tests passed :)")


if __name__ == '__main__':
    main()
