# check if there are three words in a row
def checkThreeWords(inputStr):
    count = 0
    for substring in inputStr.split():
        if substring.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


def main():
    inputString = input("Enter your string with separator as ' ' (whitespace)...\n")
    print(checkThreeWords(inputString))


if __name__ == '__main__':
    main()

