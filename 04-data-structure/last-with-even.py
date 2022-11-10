from typing import List


def findProduct(list: List[int]) -> int:
    if list == []:
        return 0
    else:
        # return a list with even indices
        even_numbers = list[::2] 
        # return a sum of elements in the list
        sum_of_even_numbers = sum(even_numbers)
        # get the last element in the original list
        last_element = list[-1]
        result = int(last_element * sum_of_even_numbers)
        return result


def main():
    print(findProduct([0, 1, 2, 3, 4, 5]))
    print(findProduct([1, 3, 5]))
    print(findProduct([]))


if __name__ == '__main__':
    main()
