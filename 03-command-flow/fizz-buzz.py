# Fizz buzz program
def check(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "Fizz Buzz"
    elif (number % 3 == 0) and (number % 5 != 0):
        return "Fizz"
    elif (number % 3 != 0) and (number % 5 == 0):
        return "Buzz"
    else:
        return str(number)


def main():
    inputValue = input()
    intNumber = int(inputValue)
    
    print(check(intNumber))


if __name__ == '__main__':
    main()
