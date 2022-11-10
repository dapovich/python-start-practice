# Fizz buzz program
def check(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "Fizz Buzz"
    elif (number % 3 == 0):
        return "Fizz"
    elif (number % 5 == 0):
        return "Buzz"
    else:
        return str(number)


def main():
    input_value = input()
    int_number = int(input_value)
    
    print(check(int_number))


if __name__ == '__main__':
    main()
