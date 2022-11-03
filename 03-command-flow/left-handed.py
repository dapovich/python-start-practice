# change all occurences of string 'right' to the 'left' in the input string with ',' separator
def changeRightLeft(input_str):
    split_str = input_str.split(",")
    for idx in range(0, len(split_str) - 1):
        split_str[idx] = split_str[idx].replace("right", "left")
    return ','.join(split_str)


def main():
    input_str = input("Input string with separator ','...\n")
    print(changeRightLeft(input_str))


if __name__ == '__main__':
    main()
