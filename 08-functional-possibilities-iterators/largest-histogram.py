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


def to_find_largest_rectangle(heights: list[int]) -> int:
    stack = []
    idx = 0
    largest_area = 0
    while idx < len(heights):
        if len(stack) == 0 or heights[stack[-1]] <= heights[idx]:
            stack.append(idx)
            idx += 1
        else:
            x = stack[-1]
            stack.pop()
            height = heights[x]
            temp = height * (idx - stack[-1] - 1) if len(stack) != 0 else height * idx
            largest_area = max(largest_area, temp)
    while len(stack) > 0:
        x = stack[-1]
        height = heights[x]
        stack.pop()
        temp = height * (len(heights) - stack[-1] - 1) if len(stack) != 0 else height * len(heights)
        largest_area = max(largest_area, temp)
    return largest_area


if __name__ == '__main__':
    print("Test 1\nInput: [5]")
    print(f"Output: {to_find_largest_rectangle([5])}")
    assert to_find_largest_rectangle([5]) == 5, print(f"ERROR: output is uncorrect.")

    print("Test 2\nInput: [5, 3]")
    print(f"Output: {to_find_largest_rectangle([5, 3])}")
    assert to_find_largest_rectangle([5, 3]) == 6, print(f"ERROR: output is uncorrect.")

    print("Test 3\nInput: [1, 1, 4, 1]")
    print(f"Output: {to_find_largest_rectangle([1, 1, 4, 1])}")
    assert to_find_largest_rectangle([1, 1, 4, 1]) == 4, print(f"ERROR: output is uncorrect.")

    print("Test 4\nInput: [1, 1, 3, 1]")
    print(f"Output: {to_find_largest_rectangle([1, 1, 3, 1])}")
    assert to_find_largest_rectangle([1, 1, 3, 1]) == 4, print(f"ERROR: output is uncorrect.")

    print("Test 5\nInput: [2, 1, 4, 5, 1, 3, 3]")
    print(f"Output: {to_find_largest_rectangle([2, 1, 4, 5, 1, 3, 3])}")
    assert to_find_largest_rectangle([2, 1, 4, 5, 1, 3, 3]) == 8, print(f"ERROR: output is uncorrect.")
