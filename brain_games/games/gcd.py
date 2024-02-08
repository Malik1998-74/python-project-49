from random import randint
import prompt


MAX_ROUNDS = 3


def divisor():
    round = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ').capitalize()
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    while round != MAX_ROUNDS:
        number_one = randint(1, 100)
        number_two = randint(1, 100)
        print(f'Question: {number_one} {number_two}')
        your_answer = prompt.integer('Your answer: ')
        while number_one != number_two:
            if number_one > number_two:
                number_one -= number_two
            else:
                number_two -= number_one
        if number_one == your_answer:
            print('Correct!')
        else:
            print(f"""
{your_answer} is wrong answer,;(. Correct answer was '{number_one}'
Let's try again, {name}!""")
            break
        round += 1
    if round == MAX_ROUNDS:
        print(f'Congratulations,{name}')
