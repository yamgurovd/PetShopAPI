import random


def random_choice(array: list, seed_for_test: int | str | bool = None) -> any:
    """Выполняется случайный выбор значения из листа"""

    random.seed(seed_for_test)
    return random.choice(array)
