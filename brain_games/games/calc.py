from brain_games.games.general_logging import logging
import random


WELCOME_TEXT_CALC: str = 'What is the result of the expression?'
symbols: list = ['+', '-', '*']


def calc():
    symbol = random.choice(symbols)
    number_one: int = random.randint(1, 10)
    number_two: int = random.randint(1, 10)
    question: str = f'{number_one} {symbol} {number_two}'
    if symbol == '+':
        right_answer: int = number_one + number_two
    elif symbol == '-':
        right_answer: int = number_one - number_two
    else:
        right_answer: int = number_one * number_two
    return question, str(right_answer)


def play():
    logging(game=calc, text=WELCOME_TEXT_CALC)
