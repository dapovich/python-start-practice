# Swap keys and values in dictionary, i.e. get the inversed dictionary


def to_inverse(phone_book: dict[str, str]) -> dict[str, str]:
    return dict(zip(phone_book.values(), phone_book.keys()))


def main():
    phone_book = {
        'Petr' : '546810',
        'Katya' : '241815',
        'Danil' : '195192',
        'Ivan' : '924919',
    }
    print(phone_book)
    print(to_inverse(phone_book))


if __name__ == '__main__':
    main()
