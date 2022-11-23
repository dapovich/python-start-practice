# Find and return a new array of not unique elements in the input list


def find_non_unique(elements: list[int]) -> list[int]:
    return [element for element in elements if elements.count(element) > 1]


def main():
    testing_list_one = find_non_unique([1, 2, 3, 1, 3])
    testing_list_two = find_non_unique([1, 2, 3, 4, 5])
    testing_list_three = find_non_unique([5, 5, 5, 5, 5])
    testing_list_four = find_non_unique([10, 9, 10, 10, 9, 8])

    expected_answer = {
        1 : [1, 3, 1, 3],
        2 : [],
        3 : [5, 5, 5, 5, 5],
        4 : [10, 9, 10, 10, 9],
    }

    assert testing_list_one == expected_answer[1], f"Answer is wrong.\n Your result: {testing_list_one}\n expected: {expected_answer[1]}"
    assert testing_list_two == expected_answer[2], f"Answer is wrong\n Your result: {testing_list_two}\n expected: {expected_answer[2]}"
    assert testing_list_three == expected_answer[3], f"Answer is wrong\n Your result: {testing_list_three}\n expected: {expected_answer[3]}"
    assert testing_list_four == expected_answer[4], f"Answer is wrong\n Your result: {testing_list_four}\n expected: {expected_answer[4]}"

    print("Tests passed :)")


if __name__ == '__main__':
    main()
