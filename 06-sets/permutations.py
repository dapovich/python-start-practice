# May don't get the idea of the task properly. Make task as I see it


def find_permutations(x: int, y: int, z: int, n: int) -> list[list[int]] | int:
    sizes = { 'x' : x, 'y' : y, 'z' : z}
    if (x + y + z) == n:
        return -1
    permutations_list = [
        [x, y, z] 
        for x in range(sizes['x'] + 1) 
        for y in range(sizes['y'] + 1) 
        for z in range(sizes['z'] + 1)
        if x + y + z != n
    ]
    return permutations_list


def main():

    args = {
        1 : { 'x' : 1, 'y' : 1, 'z' : 1, 'n' : 2},
        2 : { 'x' : 1, 'y' : 1, 'z' : 1, 'n' : 4},
        3 : { 'x' : 1, 'y' : 1, 'z' : 1, 'n' : 1},
        4 : { 'x' : 1, 'y' : 1, 'z' : 1, 'n' : 3},
    }

    answers = {
        1 : find_permutations(args[1]['x'], args[1]['y'], args[1]['z'], args[1]['n']),
        2 : find_permutations(args[2]['x'], args[2]['y'], args[2]['z'], args[2]['n']),
        3 : find_permutations(args[3]['x'], args[3]['y'], args[3]['z'], args[3]['n']),
        4 : find_permutations(args[4]['x'], args[4]['y'], args[4]['z'], args[4]['n']),
    }

    expected_answers = {
        1 : [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]],
        2 : [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]],
        3 : [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1]],
        4 : -1,
    }

    for i in range(1, len(answers) + 1):
        assert answers[i] == expected_answers[i], f"Answer is wrong\n Your result: {answers[i]}\n expected: {expected_answers[i]}"
        print(f"Test {i}:")
        print(f"Input data:\nx = {args[i]['x']}, y = {args[i]['y']}, z = {args[i]['z']}, n = {args[i]['n']}")
        print(f"Output:", answers[i])
        print(f"Expected output:", expected_answers[i], end=2*'\n')


if __name__ == '__main__':
    main()
