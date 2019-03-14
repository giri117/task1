board=['  ' for x in range(9)]

def print_board():
    row1 = '|{}|{}|{}|'.format(board[0],board[1],board[2])
    row2 = '|{}|{}|{}|'.format(board[3],board[4],board[5])
    row3 = '|{}|{}|{}|'.format(board[6],board[7],board[8])

    print()#just for having space
    print(row1)
    print(row2)
    print(row3)
    print()
    
def player_move(icon):

    if icon =='x':
        number=1
    elif icon =='y':
        number=2
    print('your turn player{}'.format(number))

    choice=int(input('Enter your move(1-9): ').strip())
    if board[choice-1]=='  ':
        board[choice-1]=icon
    else:
        print()
        print('That space is taken')

def win(icon):
    if (board[0]==icon,board[1]==icon,board[2]==icon) or\
       (board[3]==icon,board[4]==icon,board[5]==icon) or\
       (board[6]==icon,board[7]==icon,board[8]==icon) or\
       (board[0]==icon,board[3]==icon,board[6]==icon) or\
       (board[1]==icon,board[4]==icon,board[7]==icon) or\
       (board[2]==icon,board[5]==icon,board[8]==icon) or\
       (board[0]==icon,board[4]==icon,board[8]==icon) or\
       (board[2]==icon,board[4]==icon,board[6]==icon):
        return True
    else:
        return False
    


while True:
    print_board()
    player_move('x')
    print_board()
    if victory('x'):
        print('x won')
        break
    elif draw():
        print('draw')
        break
    
    player_move('o')
    if victory('y'):
        print_board()
        print('y won')
        break
    
    
