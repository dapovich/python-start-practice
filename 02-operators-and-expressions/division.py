from random import randint, randrange

def main():
    number1 = randint(5, 25)
    number2 = randrange(10, 20, 2)
    result = format(round((number1 / number2), 2))
    print(f"{number1=}\n{number2=}\n")
    print(f"{result=}")

if __name__ == '__main__':
    main()
