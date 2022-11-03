# sequence of number
def printSequence(size):
    for item in range(1, size + 1):
        print(f"{item} ", end = "")


def main():
    inputVar = input("Enter an integer number in range [1-9]...\n")
    number = int(inputVar)
    
    if number >= 1 and number <= 9:
        printSequence(number)
    else:
        print("Error: your number isn't in range [1-9].\n")
        return


if __name__ == '__main__':
    main()
