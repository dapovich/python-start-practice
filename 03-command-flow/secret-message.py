# secret message program
def main():
    inputString = input()
    # method 1
    # use generator expressions and method join
    capitalsWord = ''.join([char for char in inputString if char.isupper()])
    print(capitalsWord)
    # method 2
    capitalsWordMethod2 = ''
    for letter in inputString:
        # ord converts a character into its Unicode code
        # codes of capitals characters A - Z is being in range 65 - 90
        if ord(letter) in range(65, 91):
            capitalsWordMethod2 += letter
    print(capitalsWord)


if __name__ == '__main__':
    main()
