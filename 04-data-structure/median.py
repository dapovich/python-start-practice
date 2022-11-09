from typing import Union


def findMedian(sequence: Union[tuple[int, ...], list[int]]) -> Union[int, float]:
    if len(sequence) == 0:
        return 0

    list = sorted(sequence)
    middle = len(sequence) // 2
    if (len(sequence)) % 2 == 0:
        median = (list[middle] + list[middle-1]) / 2
        return median
    else:
        return list[middle]


def main():
    print(findMedian([1, 2, 3, 4, 5]))
    print(findMedian((3, 1, 2, 5, 3)))
    print(findMedian([1, 300, 2, 200, 1]))
    print(findMedian([3, 6, 20, 99, 10, 15]))
    print(findMedian([4, 1, 2, 6, 8, 9, 11, 12]))


if __name__ == '__main__':
    main()
