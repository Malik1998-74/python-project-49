from typing import Callable
import prompt


MAX_ROUNDS: int = 3


def logging(game: Callable, text: str) -> None:
    print('Welcome to the Brain Games!')
    name: str = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    print(text)
    rounds: int = 0
    while rounds != MAX_ROUNDS:
        number, right_answer = game()
        print(f'Question: {number}')
        user_answer: str = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"""
{user_answer} is wrong answer ;(. Correct answer was {right_answer}.
Let's try again, {name}!""")
            break
        rounds += 1
    if rounds == MAX_ROUNDS:
        print(f'Congratulations, {name}!')
