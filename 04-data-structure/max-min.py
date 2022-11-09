from typing import List
from typing import Union


def findDifferenceBtwMaxMin(list: List[Union[int, float]]) -> Union[int, float]:
    if list == []:
        return 0
    else:
        max_value = max(list)
        min_value = min(list)
        difference = round(max_value - min_value, 3)
        return difference


def main():
    print(findDifferenceBtwMaxMin([1, 2, 3]))
    print(findDifferenceBtwMaxMin([5, -5]))
    print(findDifferenceBtwMaxMin([10.2, -2.2, 0, 1.1, 0.5]))
    print(findDifferenceBtwMaxMin([]))


if __name__ == '__main__':
    main()
