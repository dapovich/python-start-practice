# Given an integer x, return true if x is a palindrome, and false otherwise.
# do task without conversion to the string

def isPalindrome(x: int) -> bool:
    input_number = x
    reversed_number = 0
    while x > 0:
        reversed_number = reversed_number * 10 + x % 10
        x //= 10
        print(x, reversed_number)
    print(input_number, reversed_number)
    return input_number == reversed_number


def main():
    print(3113, isPalindrome(3113))


if __name__ == '__main__':
    main()
