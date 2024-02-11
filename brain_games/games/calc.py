import random
import prompt


MAX_ROUNDS = 3


def result_of_expression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    symbols = ['+', '-', '*']
    rounds = 0
    while rounds != 3:
        symbol = random.choice(symbols)
        number_one = random.randint(1, 10)
        number_two = random.randint(1, 10)
        print('What is the result of the expression?')
        print(f'Question: {number_one} {symbol} {number_two}')
        user_answer = prompt.integer('Your answer: ')
        if symbol == '+':
            result = number_one + number_two
        elif symbol == '-':
            result = number_one - number_two
        else:
            result = number_one * number_two
        if user_answer == result:
            print('Correct!')
        else:
            print(f"""
{user_answer} is wrong answer ;(. Correct answer was {result}.
Let's try again, {name}!""")
            break
        rounds += 1
    if rounds == MAX_ROUNDS:
        print(f'Congratulations, {name}!')
        
