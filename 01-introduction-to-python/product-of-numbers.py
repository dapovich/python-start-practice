# function to calculate the product of digits in the number except 0
def product(number):
    # base case
    if number == 0:
        # return 1 as the last multiplier
        return 1
    if (number % 10) == 0:
        return product(number // 10)
    else:
        return ((number % 10) * product(number // 10))


def main():
    print("Enter a number:")
    number = int(input())
    print(product(number))


if __name__ == '__main__':
    main()
