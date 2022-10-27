# Make junior and junior+ tasks for inverse number
LEFT_BOUNDARY_32INT = -2147483648
RIGHT_BOUNDARY_32INT = 2147483648

def inverse(number):
    # check if the number is beyond the boundaries of the 32-bit number
    if int(number) > LEFT_BOUNDARY_32INT and int(number) < RIGHT_BOUNDARY_32INT:
        string = str(number)
        if string[0] == '-':
            concatenateString = string[1:]
            # use [::-1] to reverse string characters
            reverseString = concatenateString[::-1]
            reverseNumber = int(string[0] + reverseString)
        else:
            reverseString = string[::-1]
            reverseNumber = int(reverseString)
        return reverseNumber
    return 0


def main():
    number = int(input())
    print(inverse(number))


if __name__ == '__main__':
    main()
