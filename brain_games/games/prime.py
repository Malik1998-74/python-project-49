from brain_games.games.general_logging import logging
import random


tasks = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime():
    number = random.randint(2, 100)
    lts = []
    for char in range(2, number + 1):
        if number % char == 0:
            lts.append(char)
    if len(lts) == 1:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return str(number), right_answer


def play():
    logging(game=prime, text=tasks)
