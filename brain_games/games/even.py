from random import randint
import prompt


MAX_ROUNDS = 3


def parity_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    rounds = 0
    while rounds != MAX_ROUNDS:
        question = randint(0, 10)
        if question % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
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
