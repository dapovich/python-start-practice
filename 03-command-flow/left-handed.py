# change all occurences of string 'right' to the 'left'
def changeRightLeft(inputStr):
    splitStr = inputStr.split(",")
    for idx in range(0, len(splitStr) - 1):
        splitStr[idx] = splitStr[idx].replace("right", "left")
    return ','.join(splitStr)


def main():
    inputStr = input("Input string with separator ','...\n")
    print(changeRightLeft(inputStr))


if __name__ == '__main__':
    main()
