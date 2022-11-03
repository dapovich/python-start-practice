# Make junior and junior+ tasks for inverse number
LEFT_BOUNDARY_32INT = -2147483648
RIGHT_BOUNDARY_32INT = 2147483648

def inverse(number):
    # check if the number is beyond the boundaries of the 32-bit number
    if int(number) > LEFT_BOUNDARY_32INT and int(number) < RIGHT_BOUNDARY_32INT:
        string = str(number)
        if string[0] == '-':
            concatenated_string = string[1:]
            # use [::-1] to reverse string characters
            reversed_string = concatenated_string[::-1]
            reversed_number = int(string[0] + reversed_string)
        else:
            reversed_string = string[::-1]
            reversed_number = int(reversed_string)
        return reversed_number
    return 0


def main():
    number = int(input())
    print(inverse(number))


if __name__ == '__main__':
    main()
