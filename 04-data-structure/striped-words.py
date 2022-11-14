# Striped words program
import re


# global variables
vowels = {'a', 'e', 'i', 'o', 'u', 'y'} 
consonats = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
             'q', 'r', 's', 't', 'v', 'w', 'x', 'z'}


def count_striped_words(string: str) -> int:
    stack = []
    striped_words_counter = 0
    substring_is_a_stripped_word = True
    # Use regex expressions to split our string out with different limiters
    # TODO: how to escape of empty character '' in the splitted list
    substrings_list = re.split(r' |\?|, |_|-|!|,|\.', string)
    # To debug and see how input string is splitted
    print(substrings_list)
    for substring in substrings_list:
        # Check that substring doesn't have numbers, doesn't contain minimum two letters and isn't empty
        if substring.isalpha() and substring != '' and len(substring) > 1:
            # TODO: as there is a problem with empty character '' in the splitted list
            # should check for them
            for char in substring.lower():
                if stack == []:
                    stack.append(char)
                elif stack[-1] in consonats and char in vowels:
                    stack.append(char)
                elif stack[-1] in vowels and char in consonats:
                    stack.append(char)
                else:
                    # substring isn't a stripped word
                    substring_is_a_stripped_word = False
                    break
            if substring_is_a_stripped_word:
                striped_words_counter += 1
        stack = []
        substring_is_a_stripped_word = True

    return striped_words_counter


def main():
    print(count_striped_words("Dog,cat,mouse,bird.human."))
    print(count_striped_words("My name is ..."))
    print(count_striped_words("Hello world"))
    print(count_striped_words("A quantity of striped words."))


if __name__ == '__main__':
    main()
