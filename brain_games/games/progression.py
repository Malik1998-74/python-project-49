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
        start = random.randint(1, 3)
        stop = random.randint(30, 100)
        step = random.randint(3, 5)
        number = []
        for i in range(start, stop, step):
            number.append(str(i))
        random_index = random.randint(1, 9)
        random_value = number[random_index]
        number[random_index] = '...'
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
        print(f'Congratulations,{name}')
