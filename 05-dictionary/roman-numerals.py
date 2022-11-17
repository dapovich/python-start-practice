# Roman numerals representation for integer values
from collections import OrderedDict


# Global dictionary of roman_numerals
roman_numerals = OrderedDict()
roman_numerals = {
    1000 : 'M',
    900 : 'CM',
    500 : 'D',
    400 : 'CD',
    100 : 'C',
    90 : 'XC',
    50 : 'L',
    40 : 'XL',
    10 : 'X',
    9 : 'IX',
    5 : 'V',
    4 : 'IV',
    1 : 'I',
}


def to_roman(number: int) -> str:
    print(number)
    roman = ''
    while number:
        for digit, roman_numeral in roman_numerals.items():
            while number >= digit:
                roman += roman_numeral
                number -= digit
    return roman


def main():
    print(to_roman(3999), end='\n\n')
    print(to_roman(76), end='\n\n')
    print(to_roman(6), end='\n\n')
    print(to_roman(44), end='\n\n')
    print(to_roman(2022), end='\n\n')


if __name__ == '__main__':
    main()
