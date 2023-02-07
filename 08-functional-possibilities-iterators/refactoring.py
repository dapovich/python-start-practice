# Задача: Рефакторинг.
# Дано: неоптимальный код.
#
# Задание: оптимизировать следующий код.
#
# sentences = ['капитан джек воробей',
#              'капитан дальнего плавания',
#              'ваша лодка готова, капитан']
#
# cap_count = 0
# for sentence in sentences:
#     cap_count += sentence.count('капитан')
#
# print(cap_count)


sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']


def to_count_word(data: list[str], word='капитан') -> int:
    return sum(1 for sentence in data if word in sentence)


if __name__ == '__main__':
    print(to_count_word(sentences))
    
