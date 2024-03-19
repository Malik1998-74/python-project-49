from brain_games.games.general_logging import logging
from random import randint


tasks = 'Answer "yes" if the number is even, otherwise answer "no".'


def even():
    number = randint(0, 10)
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return str(number), right_answer


def play():
    logging(game=even, text=tasks)
