board = [[' ' for _ in range(3)] for _ in range(3)]

def draw_board():
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('-----------')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('-----------')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

def get_move(player):
    while True:
        move = input(f'{player}, enter your move (row column): ')
        try:
            row, col = map(int, move.split())
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] == ' ':
                    board[row][col] = player
                    return
                else:
                    print('That space is already occupied!')
            else:
                print('Invalid move!')
        except ValueError:
            print('Invalid input. Enter your move as two integers, separated by a space.')

def has_won(player):
    # check rows
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    # check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def main():
    while True:
        draw_board()
        get_move('X')
        if has_won('X'):
            print('X has won!')
            break
        draw_board()
        get_move('O')
        if has_won('O'):
            print('O has won!')
            break

main()
