# Created by Kyle Gabriel Galvez


def playornaw():
    decision = input("Press 'p' to play or 'q' to quit: ")
    return decision


def user1_input():
    call1 = input("Player 1! Choose a number 1-9: ")
    return call1


def user2_input():
    call2 = input("Player 2! Choose a number 1-9: ")
    return call2


def display_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5])
    print(board[6], '|', board[7], '|', board[8])


print('Welcome to Tic-Tac-Toe!!')
print()
play = playornaw()
print()
print('''Chosen number is represented below on board
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9''')
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

while play != 'q':
    if play == 'p':
        pass
    elif play == 'q':
        break
    else:
        print('Invalid input. Try again.')
        print()
        play = playornaw()
        continue
    display_board()
    play1_input = ''
    play2_input = ''

    # player 1 changes board
    while not play1_input.isnumeric():
        play1_input = user1_input()
        if len(play1_input) == 1 and play1_input.isnumeric():
            inp1 = int(play1_input)
            inp1 -= 1
            if board[inp1] == '-':
                board[inp1] = 'X'
            else:
                print('Invalid input. Try again.\n')
                play1_input = ''
                display_board()
                continue
        else:
            print('Invalid input. Try again.')

    # player 1 wins
    possible_wins1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    row1 = [0, 1, 2]
    player1_wins = False
    # two for loops index the board list to check if there are three in a row
    for i in range(len(possible_wins1)):
        counter1 = 0
        wins_check = possible_wins1[i]
        for j in range(len(row1)):
            win_check = wins_check[j]
            if board[win_check] == 'X':
                counter1 += 1
        if counter1 == 3:
            player1_wins = True
            break
        else:
            pass
    # displays win message and resets counter and board
    if player1_wins:
        display_board()
        print('Player 1 WINS!!\n')
        play = input("Press 'p' to play again or 'q' to quit: ")
        board = ['-', '-', '-',
                 '-', '-', '-',
                 '-', '-', '-']
        continue

    display_board()

    # player 2 changes board
    while not play2_input.isnumeric():
        play2_input = user2_input()
        if len(play2_input) == 1 and play2_input.isnumeric():
            inp2 = int(play2_input)
            inp2 -= 1
            if board[inp2] == '-':
                board[inp2] = 'O'
            else:
                print('Invalid input. Try again.\n')
                play2_input = ''
                display_board()
                continue
        else:
            print('Invalid input. Try again.')

# player 2 wins
    possible_wins2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
    row2 = [0, 1, 2]
    player2_wins = False
    for i in range(len(possible_wins2)):
        counter2 = 0
        wins_check = possible_wins2[i]
        for j in range(len(row2)):
            win_check = wins_check[j]
            if board[win_check] == 'O':
                counter2 += 1
        if counter2 == 3:
            player2_wins = True
            break
        else:
            pass
    # displays win message and resets counter and board
    if player2_wins:
        display_board()
        print('Player 2 WINS!!\n')
        play = input("Press 'p' to play again or 'q' to quit: ")
        board = ['-', '-', '-',
                 '-', '-', '-',
                 '-', '-', '-']
        continue

print('Thanks for playing!')
