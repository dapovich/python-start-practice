# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
def reverseVowels(s: str) -> str:
    vowels = {'a','A','e','E','i','I','o','O','u','U'}
    s_list = list(s)

    # moving from left side and right side until they will meet
    left = 0 
    right = len(s) - 1
    while left < right:
        if s_list[left] in vowels and s_list[right] in vowels:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            right -= 1
            left += 1
        elif s_list[left] not in vowels:
            left += 1
        else:
            right -= 1

    # join together modified s_list
    return ''.join(s_list)


def main():
    string = "hello"
    print(reverseVowels(string))


if __name__ == '__main__':
    main()
