from random import randint

board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def board_isfull():
    for i in board:
        if i ==' ':
            return False
        continue
    return True

def replay():
    r='o'
    while r not in ['y','n']:
        r=input("want to replay 'y' if not 'n':")
    if r=='y':
        return True
    else:
        return False

def display(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-----")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-----")
    print(board[6]+"|"+board[7]+"|"+board[8])


def check_win(charac):
    #t=[[board[0],board[1],board[2]],[board[3],board[4],board[5]],[board[6],board[7],board[8]],[board[0],board[3],board[6]],[board[1],board[4],board[7]],[board[2],board[5],board[8]],[board[0],board[4],board[8]],[board[2],board[4],board[8]]]
    if (board[0]==board[1]==board[2]==charac) or (board[3]==board[4]==board[5]==charac) or (board[6]==board[7]==board[8]==charac) or (board[0]==board[3]==board[6]==charac) or (board[1]==board[4]==board[7]==charac) or (board[2]==board[5]==board[8]==charac) or (board[0]==board[4]==board[8]==charac) or (board[2]==board[4]==board[6]==charac):
        return True
    else:
        return False

def player_input():
    get=0

    while get not in ['x','o']:
        get=input("Select 'x' or'o' :")
    return get

def player_marker(board,sym,pos):
    board[pos-1]=sym
    return board

def choose_first():
    return randint(1,3)

def space_check( position):
    if board[position-1]==' ':
        return True
    else:
        return False

def player_choice():
    '''x=-1
    while x not in range(1,10):
        x=int(input("enter position"))
    if not space_check(x):
        print("selected position is filled select another position")
        player_choice()
    else:
        return x'''
    n=0
    while n not in range(1,10):
        n=int(input("enter position "))
        if not space_check(n):
            print("selected position is filled select another position")
            n=0
    return n

print('Welcome to Tic Tac Toe!')
while True:
    r=choose_first()
    if r==1:
        player1=player_input()
        if player1=='x':
            player2='o'
        else:
            player2='x'
    else:
        player2=player_input()
        if player2=='x':
            player1='o'
        else:
            player1='x'
    game_on=True
    display(board)
    while game_on:
        player_marker(board,player1,player_choice())
        display(board)
        if check_win(player1):
            print("player1 {} win".format(player1))
            game_on=False
            break
        elif check_win(player2):
            print("player2 {} win".format(player2))
            game_on=False
            break
        elif board_isfull():
            print("both have lost the game")
            break
        player_marker(board,player2,player_choice())
        display(board)
        if check_win(player1):
            print("player1 {} win".format(player1))
            game_on=False
            break
        elif check_win(player2):
            print("player2 {} win".format(player2))
            game_on=False
            break
        elif board_isfull():
            print("both have lost the game")
            break

    if not replay():
        break
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
print("Game is completed")