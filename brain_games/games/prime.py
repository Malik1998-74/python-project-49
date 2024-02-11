import random
import prompt
import math

max_round = 3


def prime_number():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    round = 0
    while round != max_round:
        number = random.randint(2, 100)
        print(f'Question: {number}')
        lts = []
        for char in range(2, int(math.sqrt(number)) + 1):
            if number % char == 0:
                lts.append(char)
        if len(lts) == 1:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct')
        else:
            print(f"""{user_answer} is wrong answer ;(.
Correct answer was {right_answer}. Let's try again, {name}!""")
            break
        round += 1
    if round == max_round:
        print(f'Congratulations, {name}!')
