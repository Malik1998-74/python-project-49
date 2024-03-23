from brain_games.games.general_logging import logging
from random import randint


WELCOME_TEXT_EVEN: str = 'Answer "yes" if the number is even, ' \
                         'otherwise answer "no".'


def even():
    number: int = randint(0, 10)
    if number % 2 == 0:
        right_answer: str = 'yes'
    else:
        right_answer: str = 'no'
    return str(number), right_answer


def play():
    logging(game=even, text=WELCOME_TEXT_EVEN)
