from brain_games.games.general_logging import logging
from random import randint


tasks = 'Find the greatest common divisor of given numbers.'


def gcd():
    number_one = randint(1, 20)
    number_two = randint(1, 20)
    question = f'{number_one} {number_two}'
    while number_one != number_two:
        if number_one > number_two:
            number_one -= number_two
        else:
            number_two -= number_one
    return question, str(number_one)


def play():
    logging(game=gcd, text=tasks)
