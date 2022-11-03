# number estimation program
import ast


def estimateNumber(number):
    if number % 2 != 0:
        return "Bad :("
    elif number >= 2 and number <= 5 and number % 2 == 0:
        return "Not bad"
    elif number >= 6 and number <= 20 and number % 2 == 0:
        return "So-so"
    elif number > 20 and number % 2 == 0:
        return "Great :)"
    else:
        return None


def main():
    number = input("Input your number (int or float)...\n")
    try:
        checkInput = ast.literal_eval(number)
    except Exception as err:
        print("Error: your input is an invalid type.\n", err)
    else:
        if type(checkInput) is float:
            print(estimateNumber(float(number)))
        elif type(checkInput) is int:
            print(estimateNumber(int(number)))


if __name__ == '__main__':
    main()
