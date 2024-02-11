import random
import prompt


MAX_ROUNDS = 3


def progress():
    print('Welcome to the Brain Games!')
    name = prompt.string('May i have your name? ').capitalize()
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    round = 0
    while round != MAX_ROUNDS:
        start = random.randint(2, 30)
        step = random.randint(2, 4)
        number = []
        for i in range(1, 11):
            new = start + (i - 1) * step
            number.append(str(new))
        random_index = random.randint(0, 9)
        random_value = number[random_index]
        number[random_index] = '..'
        result = " ".join(number)
        print(f'Question: {result}')
        your_answer = prompt.string('Your answer: ')
        if your_answer == random_value:
            print('Correct!')
        else:
            print(f"""
{your_answer} is wrong answer,;(. Correct answer was '{random_value}'
Let's try again, {name}!""")
            break
        round += 1
    if round == MAX_ROUNDS:
        print(f'Congratulations, {name}!')
