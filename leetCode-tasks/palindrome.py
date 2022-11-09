# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x: int) -> bool:
    string = str(x)
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False


def main():
    print(121, isPalindrome(121))
    print(545, isPalindrome(545))
    print(1001, isPalindrome(1001))
    print(808808, isPalindrome(808808))
    print(1204905, isPalindrome(1204905))
    

if __name__ == '__main__':
    main()
