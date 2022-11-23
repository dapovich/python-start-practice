# Roman numerals representation for integer values
from collections import OrderedDict


# Global dictionary of roman_numerals
roman_numerals = OrderedDict()
roman_numerals[1000] = 'M'
roman_numerals[900] = 'CM'
roman_numerals[500] = 'D'
roman_numerals[400] = 'CD'
roman_numerals[100] = 'C'
roman_numerals[90] = 'XC'
roman_numerals[50] = 'L'
roman_numerals[40] = 'XL'
roman_numerals[10] = 'X'
roman_numerals[9] = 'IX'
roman_numerals[5] = 'V'
roman_numerals[4] = 'IV'
roman_numerals[1] = 'I'


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
