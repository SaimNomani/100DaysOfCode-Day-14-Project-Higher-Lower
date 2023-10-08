import random

from art import logo, vs
from game_data import data


# from replit import clear


def generate_account():
    account = random.choice(data)
    return account


def compare(opt_a, opt_b):
    if opt_a['follower_count'] > opt_b['follower_count']:
        return 'A'
    return 'B'


def play():
    print(logo)
    score = 0
    should_continue = True
    should_restart = False
    option_a = generate_account()
    option_b = generate_account()
    while should_continue:
        while option_a['name'] == option_b['name']:
            option_b = generate_account()
        result = compare(option_a, option_b)
        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
        print(vs)
        print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")
        answer = (input("Who has more followers? Type 'A' or 'B': ")).upper()
        # clear()
        print(logo)
        if answer == result:
            score += 1
            print(f"You are right, current score: {score}")
            if answer == 'B' and result == 'B':
                option_a = option_b
            option_b = generate_account()
        else:
            should_continue = False
            print(f"Sorry, that's wrong, final score: {score}")
    choice = (input("Do you want to restart the game type 'y' or 'n' to exit: ")).lower()
    if choice == 'y':
        should_restart = True
        play()


play()
