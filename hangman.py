# Created by Kyle Gabriel Galvez

import random


def stand():
    print('  _______')
    print(' /      |')
    print(' |')
    print(' |')
    print(' |')
    print(' |')
    print(' |')
    print('/ \\')


def head():
    print('  _______')
    print(' /     _|_')
    print(' |    |___|')
    print(' |      ')
    print(' |')
    print(' |')
    print(' |')
    print('/ \\')


def body():
    print('  _______')
    print(' /     _|_')
    print(' |    |___|')
    print(' |      |')
    print(' |      |')
    print(' |      |')
    print(' |')
    print('/ \\')


def leg1():
    print('  _______')
    print(' /     _|_')
    print(' |    |___|')
    print(' |      |')
    print(' |      |')
    print(' |      |')
    print(' |     /')
    print('/ \\')


def leg2():
    print('  _______')
    print(' /     _|_')
    print(' |    |___|')
    print(' |      |')
    print(' |      |')
    print(' |      |')
    print(' |     / \\')
    print('/ \\')


def arm1():
    print('  _______')
    print(' /     _|_')
    print(' |    |___|')
    print(' |      |')
    print(' |     /|')
    print(' |    / |')
    print(' |     / \\')
    print('/ \\')


def arm2():
    print('  _______')
    print(' /     _|_')
    print(' |    |___|')
    print(' |      |')
    print(' |     /|\\')
    print(' |    / | \\')
    print(' |     / \\')
    print('/ \\')


# input word
def word_choice():
    word_bank = ['BEAUTIFUL', 'RHYME', 'SPRING', 'APRIL', 'FIRE', 'SCARF', 'WOOL', 'ICE']
    bank_choice = random.choice(word_bank)
    return bank_choice


# prompt to guess letter
def letter_guess():
    letter_inp = input('Guess a letter: ')
    return letter_inp


# hangman game
def hangman_game():
    print('Welcome to Hangman!!')
    print()
    next_thing = input("Press 'p' to play or 'q' to quit: ")

    while next_thing != 'q':
        if next_thing == 'p':
            pass
        elif next_thing != 'q':
            print('Invalid Input.')
            next_thing = input("Press 'p' to play or 'q' to quit: ")
            continue

        chosen_word = word_choice()
        blur_word = '- ' * len(chosen_word)
        split_word = list('-' * len(chosen_word))
        wrong_count = 0
        used_letters = ''
        letter = ''
        while '-' in blur_word:
            print('You have used these letters:', used_letters)

            # 6 chances to be wrong (hangman drawing)
            if wrong_count == 0:
                stand()
            elif wrong_count == 1:
                head()
            elif wrong_count == 2:
                body()
            elif wrong_count == 3:
                leg1()
            elif wrong_count == 4:
                leg2()
            elif wrong_count == 5:
                arm1()
            elif wrong_count == 6:
                arm2()
                break

            print('Current Word:', blur_word)
            new_split = list(chosen_word)
            letter = letter_guess()
            print()
            # same letter is inputted again
            if letter in list(used_letters):
                print('You already used that letter. Try again.')
                print()
                continue
            # input is greater than 1 letter or is not a letter
            if len(letter) > 1 or not letter.isalpha():
                print('Invalid input. Try again.')
                print()
                continue
            # input is not capitalized
            if not letter.isupper():
                print('Guessed letters must be capitalized.')
                print()
                continue
            # check input is in word
            i = 0
            while i < len(split_word):
                if new_split[i] == letter:
                    split_word[i] = letter
                elif split_word[i].isalpha():
                    i += 1
                    continue
                else:
                    split_word[i] = '-'
                i += 1
            # add inputted letters to letter list
            used_letters += letter
            # increment wrong counter
            if letter not in list(chosen_word):
                wrong_count += 1
            # make word as list into string
            blur_word = ' '.join(split_word)

        print()
        if wrong_count == 6:
            print('You have used these letters:', used_letters)
            print('Current Word:', blur_word)
            print('The word was', chosen_word)
            print('You LOST!! HAHAHA')
            print()
            next_thing = input("Press 'p' to play again or 'q' to quit: ")
            continue
        else:
            print('You have used these letters:', used_letters)
            print('Current Word:', blur_word)

            print('You WON!! WHHOOOOOOO')
            print()
            next_thing = input("Press 'p' to play again or 'q' to quit: ")
            continue
    print('Thanks for playing!')
