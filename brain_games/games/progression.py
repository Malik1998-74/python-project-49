from brain_games.games.general_logging import logging
import random


tasks = 'What number is missing in the progression?'


def progression():
    start = random.randint(2, 30)
    step = random.randint(2, 4)
    number = []
    for i in range(1, 11):
        new = start + (i - 1) * step
        number.append(str(new))
    random_index = random.randint(0, 9)
    random_value = number[random_index]
    number[random_index] = '..'
    result = " ".join(number)
    return result, random_value


def play():
    logging(game=progression, text=tasks)
