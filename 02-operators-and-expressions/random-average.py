from random import randint, randrange


def main():
    number1 = randrange(1, 10, 1)
    number2 = randint(1, 15)
    number3 = randint(1, 20)
    average = (number1 + number2 + number3) / 3
    print(f"{number1=}\n{number2=}\n{number3=}\n\n{average=}")


if __name__ == '__main__':
    main()
