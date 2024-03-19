from brain_games.games.general_logging import logging
import random


tasks = 'What is the result of the expression?'
symbols = ['+', '-', '*']


def calc():
    symbol = random.choice(symbols)
    number_one = random.randint(1, 10)
    number_two = random.randint(1, 10)
    question = f'{number_one} {symbol} {number_two}'
    if symbol == '+':
        right_answer = number_one + number_two
    elif symbol == '-':
        right_answer = number_one - number_two
    else:
        right_answer = number_one * number_two
    return question, str(right_answer)


def play():
    logging(game=calc, text=tasks)
