from brain_games.games.general_logging import logging
import random


WELCOME_TEXT_PRIME: str = 'Answer "yes" if given number is prime. ' \
                          'Otherwise answer "no".'


def prime():
    number: int = random.randint(2, 100)
    lts: list = [char for char in range(2, number + 1) if not number % char]
    if len(lts) == 1:
        right_answer: str = 'yes'
    else:
        right_answer: str = 'no'
    return str(number), right_answer


def play():
    logging(game=prime, text=WELCOME_TEXT_PRIME)
