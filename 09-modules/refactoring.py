# 3. Рефакторинг.
# Дано: неоптимальный код.
#
# Задание: оптимизировать следующий код.
# def responses_creator(item_ids):
#     item_ids = [None] if item_ids is None else item_ids
#
#     responses = []
#     for item_id in item_ids:
#         new_response = dict(item_id=item_id)
#         responses.append(new_response)
#     return responses


def responses_creator(item_ids=None):
    """Return a list of responses"""
    # We need to check if parameter item_ids is None as it's noniterable object
    if item_ids is None:
        return item_ids
    # Use list comprehension to create the list
    return [dict(item_id=item_id) for item_id in item_ids]


if __name__ == "__main__":
    print(responses_creator([120, 5523, 42, 9, 85]))
