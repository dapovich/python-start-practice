from typing import Union


def smartSort(elements: tuple[int, ...]) -> Union[list[int], tuple[int]]:
    list_of_numbers = list(elements)
    list_of_numbers.sort(key=abs)

    return list_of_numbers


def main():
    print(smartSort((-20, -5, 10, 15)))
    print(smartSort((1, 2, 3, 0)))
    print(smartSort((-1, -2, -3, 0)))


if __name__ == '__main__':
    main()
