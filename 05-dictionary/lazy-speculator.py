# Consider the bank with best offering
# Global dictionary
rates = {
    'Sberbank' : 55.8,
    'VTB24' : 53.91,
    'SovkomBank' : 54.9,
    'Rosbank' : 58.54,
    'TinkoffBank' : 51,
}


def determine_best_offer(rates: dict[str, int | float]) -> tuple[str, int | float]:
    best_bank = min(rates, key=lambda key: rates[key])
    best_offer = rates[best_bank]
    return (best_bank, best_offer)


def main():
    print(determine_best_offer(rates))


if __name__ == '__main__':
    main()
