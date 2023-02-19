# 6. Самый большой прямоугольник.
#
# Дано: список высот всех столбцов в гистограмме (список целых чисел).
#
# Задание: У вас есть гистограмма. Попробуйте найти размер самого большого прямоугольника, который можно построить из столбцов гистограммы.

# Примеры:
#     to_find_largest_rectangle([5]) == 5
#     to_find_largest_rectangle([5, 3]) == 6
#     to_find_largest_rectangle([1, 1, 4, 1]) == 4
#     to_find_largest_rectangle([1, 1, 3, 1]) == 4
#     to_find_largest_rectangle([2, 1, 4, 5, 1, 3, 3]) == 8


# TODO: Check whether it could be solved with map, reduce, filter function or other functools
def to_find_largest_rectangle(heights: list[int]) -> int:
    # Contains the index of histogram
    stack = []
    idx = 0
    largest_area = 0
    while idx < len(heights):
        if len(stack) == 0 or heights[stack[-1]] <= heights[idx]:
            stack.append(idx)
            idx += 1
        else:
            jdx = stack[-1]
            stack.pop()
            height = heights[jdx]
            candidate_height = height * (idx - stack[-1] - 1) if len(stack) != 0 else height * idx
            largest_area = max(largest_area, candidate_height)
    while len(stack) > 0:
        jdx = stack[-1]
        height = heights[jdx]
        stack.pop()
        candidate_height = height * (len(heights) - stack[-1] - 1) if len(stack) != 0 else height * len(heights)
        largest_area = max(largest_area, candidate_height)
    return largest_area


if __name__ == '__main__':
    print("Test 1\nInput: [5]")
    print(f"Output: {to_find_largest_rectangle([5])}\n")
    assert to_find_largest_rectangle([5]) == 5, print(f"ERROR: output is uncorrect.")

    print("Test 2\nInput: [5, 3]")
    print(f"Output: {to_find_largest_rectangle([5, 3])}\n")
    assert to_find_largest_rectangle([5, 3]) == 6, print(f"ERROR: output is uncorrect.")

    print("Test 3\nInput: [1, 1, 4, 1]")
    print(f"Output: {to_find_largest_rectangle([1, 1, 4, 1])}\n")
    assert to_find_largest_rectangle([1, 1, 4, 1]) == 4, print(f"ERROR: output is uncorrect.")

    print("Test 4\nInput: [1, 1, 3, 1]")
    print(f"Output: {to_find_largest_rectangle([1, 1, 3, 1])}\n")
    assert to_find_largest_rectangle([1, 1, 3, 1]) == 4, print(f"ERROR: output is uncorrect.")

    print("Test 5\nInput: [2, 1, 4, 5, 1, 3, 3]")
    print(f"Output: {to_find_largest_rectangle([2, 1, 4, 5, 1, 3, 3])}\n")
    assert to_find_largest_rectangle([2, 1, 4, 5, 1, 3, 3]) == 8, print(f"ERROR: output is uncorrect.")

    print("Tests are passed :)")
