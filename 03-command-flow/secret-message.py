# secret message program
def main():
    input_string = input()
    # method 1
    # use generator expressions and method join
    capitals_word = ''.join([char for char in input_string if char.isupper()])
    print(capitals_word)
    # method 2
    # capitals_word = ''
    # for letter in input_string:
    #     # ord converts a character into its Unicode code
    #     # codes of capitals characters A - Z is being in range 65 - 90
    #     if ord(letter) in range(65, 91):
    #         capitals_word += letter
    # print(capitals_word)


if __name__ == '__main__':
    main()
