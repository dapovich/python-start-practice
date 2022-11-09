# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dict = {}
    for key, value in enumerate(nums):
        difference = target - value
        if difference in dict:
            return [dict[difference], key]
        dict[value] = key
        print(dict)
    return []


def main():
    list_1 = [1, 5, 6, 2, 3, 8, 10, 15, 13, 11, 10, 0, 0, 4, 5, 2, 1]
    target_1 = 6
    print(twoSum(list_1, target_1))


if __name__ == '__main__':
    main()
