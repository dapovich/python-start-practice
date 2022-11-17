# Consider the result of the tic-tac-toe game


def to_determine_result(data: list[str]) -> str:
    for row in range(len(data)):
        # check for rows
        if data[row][0] == data[row][1] == data[row][2]:
            return f"-> {data[row][0]}"
        # check for columns
        if data[0][row] == data[1][row] == data[2][row]:
            return f"-> {data[0][row]}"
    # check diagonals
    if data[0][0] == data[1][1] == data[2][2]:
        return f"-> {data[0][0]}"
    if data[2][0] == data[1][1] == data[0][2]:
        return f"-> {data[2][0]}"

    # if none of the conditions passed
    return "-> D"

def main():
    data_test1 = [
        "X.O",
        "XX.",
        "XOO"
    ]
    data_test2 = [
        "OO.",
        "XOX",
        "XOX"
    ]
    data_test3 = [
        "OOX",
        "XXO",
        "OXX"
    ]
    print("Test 1:",to_determine_result(data_test1))
    print("Test 2:",to_determine_result(data_test2))
    print("Test 3:",to_determine_result(data_test3))


if __name__ == '__main__':
    main()
