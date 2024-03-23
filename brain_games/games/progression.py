from brain_games.games.general_logging import logging
import random


WELCOME_TEXT_PROGRESSION: str = 'What number is missing in the progression?'


def progression():
    start: int = random.randint(2, 30)
    step: int = random.randint(2, 4)
    number: list = [str(start + (i - 1) * step) for i in range(1, 11)]
    random_index: int = random.randint(0, 9)
    random_value: str = number[random_index]
    number[random_index] = '..'
    result: str = " ".join(number)
    return result, random_value


def play():
    logging(game=progression, text=WELCOME_TEXT_PROGRESSION)
