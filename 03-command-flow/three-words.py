# check if there are three words in a row
def checkThreeWords(input_string):
    count = 0
    for substring in input_string.split():
        if substring.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False


def main():
    input_string = input("Enter your string with separator as ' ' (whitespace)...\n")
    print(checkThreeWords(input_string))


if __name__ == '__main__':
    main()

