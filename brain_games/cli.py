import prompt


def welcome_user():
    name = prompt.string('May I have your name? ').capitalize()
    print(f'Hello, {name}!')
