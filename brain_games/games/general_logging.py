import prompt


MAX_ROUNDS = 3


def logging(game, text):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
    print(text)
    rounds = 0
    while rounds != MAX_ROUNDS:
        number, right_answer = game()
        print(f'Question: {number}')
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