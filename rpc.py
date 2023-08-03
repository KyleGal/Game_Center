# Created by Kyle Gabriel Galvez

import random
import time


def user_choice():
    inp = input("Choose ROCK, PAPER, or SCISSORS, or press 'q' to quit:")
    return inp


def comp_choice():
    word = ['ROCK', 'PAPER', 'SCISSORS']
    word = random.choice(word)
    return word


def computation(user, computer):
    if user == computer:
        print('Tie!\n')
    elif (user == 'ROCK' and computer == 'PAPER') or (user == 'PAPER' and computer == 'SCISSORS') \
            or (user == 'SCISSORS' and computer == 'ROCK'):
        print('You Lose!\n')
    elif (user == 'ROCK' and computer == 'SCISSORS') or (user == 'PAPER' and computer == 'ROCK') \
            or (user == 'SCISSORS' and computer == 'PAPER'):
        print('You Win!\n')


def count():
    print('Rock...')
    time.sleep(2)
    print('Paper...')
    time.sleep(2)
    print('Scissors...')
    time.sleep(1)


def rpc_game():
    print('Welcome to Rock Paper Scissors!!')
    print()
    valid_user_inputs = ('ROCK', 'PAPER', 'SCISSORS', 'q')
    user_input = ''
    while user_input != 'q':
        user_input = user_choice()                  # asks user input
        if user_input not in valid_user_inputs:     # checks if user input is invalid
            print('Invalid input. Try again.\n')
            continue
        elif user_input == 'q':
            print('Thanks for playing!')
            break
        count()                                     # Rock... Paper... Scissors...
        computer_input = comp_choice()              # computer makes choice
        print('SHOOOT!!!')
        time.sleep(1.5)
        print()
        print('User:', user_input)                  # print user choice
        print('Comp:', computer_input, '\n')        # prints computer choice
        time.sleep(0.5)
        computation(user_input, computer_input)     # computes result
