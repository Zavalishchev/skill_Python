board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("  0 1 2")
    for i in range(3):
        row = [str(i)]
        row.extend(board[i])
        print(' '.join(row))

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

current_player = 'X'
while True:
    print_board(board)
    while True:
        row = int(input(f'Игрок {current_player}, выберите строку (0, 1, 2): '))
        col = int(input(f'Игрок {current_player}, выберите столбец (0, 1, 2): '))
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            break
        else:
            print("Некорректный ход. Попробуйте ещё раз.")

    board[row][col] = current_player
    if check_win(board, current_player):
        print_board(board)
        print(f'Победил игрок {current_player}!')
        break
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        print_board(board)
        print("Ничья!")
        break
    current_player = 'X' if current_player == 'O' else 'O'
