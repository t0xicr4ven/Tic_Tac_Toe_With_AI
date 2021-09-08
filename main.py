import random
board = ['-' for x in range(9)]


def show_board():
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2] + "     1|2|3")
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5] + "     4|5|6")
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8] + "     7|8|9")


def get_random_move(move_list):
    leng = len(move_list)
    ran = random.randrange(0, leng)
    return move_list[ran]

def ai_move(bo):
    # get spaces left to make a move
    move = None
    moves_left = [x for x, value in enumerate(bo) if value == '-']
    # check if game can be won
    for letter in ['O','X']:
        for i in moves_left:
            board_copy = bo[:]
            board_copy[i] = letter
            if check_board(board_copy, letter):
                move = i
                return move
    # see if we can go in a corner
    corners_free = []
    for i in moves_left:
        if i in [0,2,6,8]:
            corners_free.append(i)
    if len(corners_free) > 0:
        move = get_random_move(corners_free)
        return move
    # try center
    if 5 in moves_left:
        move = 5
        return move

    # last we go for an edge
    edges_free = []
    for i in moves_left:
        if i in [1,3,5,7]:
            edges_free.append(i)
    if len(edges_free) > 0:
        move = get_random_move(edges_free)

    return move


def space_is_free(bo, move):
    return (bo[move] == '-') 


def update_board(move, let):
    board[move] = let


def is_board_full(bo):
    if bo.count('-') > 0:
        return False
    else:
        return True


def check_board(bo, letter):
    # check horizontal
    return (bo[0] == letter and bo[1] == letter and bo[2] == letter) or (bo[3]
             == letter and bo[4] == letter and bo[5] == letter) or (bo[6] ==
                     letter and bo[7] == letter and bo[8] == letter) or (bo[0]
                             == letter and bo[3] == letter and bo[6] == letter) or (bo[1] == letter and bo[4] == letter and bo[7] == letter) or (bo[2] == letter and bo[5] == letter and bo[8] == letter) or (bo[0] == letter and bo[4] == letter and bo[8] == letter) or (bo[2] == letter and bo[4] == letter and bo[6] == letter)


def get_player_one_move():
    run = True
    while run:
        move = input("Your move, select a position - (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                move = move - 1
                if space_is_free(board, move):
                    run = False
                    update_board(move, 'X')
                else:
                    print('Sorry this spot has been used')
            else:
                print('Number has to be with in the range of 1-9')
        except:
            print('entry has to be a number!')

def get_player_two_move():
    player_move = input("Your move player two: ")
    if player_move not in "1,2,3,4,5,6,7,8,9":
        print("hey invalid choice try again")
        get_player_two_move()
    else:
        update_board(player_move, 2)


def main():
    print('Welcome to Tic Tac Toe, Good Luck!')
    show_board()
    
    while not (is_board_full(board)):
        if not(check_board(board, 'O')):
            get_player_one_move()
            show_board()
        else:
            print('Sorry You Lost!')
            break
        
        if not(check_board(board, 'X')):
            move = ai_move(board)
            if move is None:
                print('Game is a tie!!')
            else:
                update_board(move, 'O')
                show_board()
                print('The computer placed an \'O\' in position', move + 1, ':')
        else:
            print('Congrats you beat the computer!!')
            break
    if is_board_full(board):
        print('Game is a tie!!')


while True:
    answer = input('Do you want to play again? (Y/N) ')
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = ['-' for x in range(9)]
        main()
    else:
        break
