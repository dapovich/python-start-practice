# Get the dictionary from the two lists: list of dates and list of rates


def to_dictionary(keys: list[str], values: list[int | float]) -> dict[str, int | float]:
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]

    return result_dict


def main():
    dates = ['2017-03-01', '2017-03-02', '2017-03-04', '2017-03-08']
    rates = [55.7, 55.2, 54.98, 55.0]
    print(dates, rates, sep='\n', end='\n\n')

    print(to_dictionary(dates, rates))


if __name__ == '__main__':
    main()
