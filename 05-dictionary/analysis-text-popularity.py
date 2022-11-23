# Analysis of chars and words popularity in the input string
import re


def find_words_popularity(input_string: str) -> dict[str, int]:
    print(f"Input string: {input_string}")
    # use punctuation chars: ',.?!-;' as delimiters using regex
    splitted_words = re.split(r', |,| |\.', input_string)
    words_popularity = {}

    for word in splitted_words:
        # TODO: the problem with dot at the end of the string;
        # if there is a dot at the end of string, it will splitted as an empty char '' at the end of splitted list
        if word == '':
            continue
        elif word not in words_popularity:
            words_popularity[word] = 1
        else:
            words_popularity[word] += 1
    
    return words_popularity


def find_chars_popularity(input_string: str) -> dict[str, int]:
    print(f"Input string: {input_string}")
    list_string = list(input_string)
    chars_popularity = {}
    for char in list_string:
        if char.isalpha():
            if not char in chars_popularity:
                chars_popularity[char] = 1
            else:
                chars_popularity[char] += 1

    return chars_popularity


def main():
    test_string1 = "hello, word of word"
    test_string2 = "return a value for a value to return"
    test_string3 = "tomato task"
    test_string4 = "soft skill sausage"

    print(find_words_popularity(test_string1), end="\n\n")
    print(find_words_popularity(test_string2), end="\n\n")
    print(find_chars_popularity(test_string3), end="\n\n")
    print(find_chars_popularity(test_string4), end="\n\n")


if __name__ == '__main__':
    main()
