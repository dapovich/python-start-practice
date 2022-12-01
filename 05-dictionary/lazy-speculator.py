# Consider the bank with best offering
# Global dictionary
rates = {
    'Sberbank' : 55.8,
    'VTB24' : 53.91,
    'SovkomBank' : 54.9,
    'Rosbank' : 58.54,
    'TinkoffBank' : 51,
    'Jamaika' : 51,
    'ECA' : 50
}


def determine_best_offer(rates: dict[str, int | float]) -> tuple[str, int | float]:
    return min(rates.items(), key=lambda key: key[1])


def main():
    print(determine_best_offer(rates))


if __name__ == '__main__':
    main()
