# Created by Kyle Gabriel Galvez

import hangman
import rpc
import madlibs


def menu_output():
    print()
    print("Game list:\n"
          "Hangman - 'H'\n"
          "Madlibs - 'M'\n"
          "Rock, Paper, Scissors - 'R'\n"
          "Tic Tac Toe - 'T'")


def game(chosen_game):
    if chosen_game == 'H':
        hangman.hangman_game()
    elif chosen_game == 'M':
        madlibs.madlibs_game()
    elif chosen_game == 'R':
        rpc.rpc_game()
    elif chosen_game == 'T':
        import tictactoe
    elif chosen_game == 'q':
        pass
    else:
        print('\nInvalid input. Try again.\n')


print("Welcome to Kyle's Game Room!!")
game_choice = ''
while game_choice != 'q':
    menu_output()
    game_choice = input("\nChoose a game or press 'q' to quit: ")
    print()
    game(game_choice)
print('Have a nice day!')
