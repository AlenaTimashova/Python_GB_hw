# Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

def print_board(lst):
    for i in range(3):
        for j in range(3):
            print(lst[i][j], end=' ')
        print()

def insert_symbol(lst, position, symbol):
    for i in range(3):
        if position in lst[i]:
            index = lst[i].index(position)
            lst[i].remove(position)
            lst[i].insert(index, symbol)
    print_board(lst)

def check_move(x, lst):
    if 0 < x < 10:
        for i in range(len(lst)):
            if x in lst[i]:
                return True
    else:
        return False
    
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_player = True
count = 0
win = False

print_board(board)

while count < 9 and win == False:
    
    # ход одного из игроков:

    if first_player:
        player_move = int(input('Ходит первый игрок. Введите номер позиции, в которую Вы хотите поставить X: '))
        if check_move(player_move, board):
            insert_symbol(board, player_move, 'X')
            first_player = False
            count += 1
        else:
            print('Неверный ввод. Попробуйте еще раз')             
    else:
        player_move = int(input('Ходит второй игрок. Введите номер позиции, в которую Вы хотите поставить О: '))
        if check_move(player_move, board):
            insert_symbol(board, player_move, 'O')
            first_player = True
            count += 1
        else:
            print('Неверный ввод. Попробуйте еще раз')
    
    # проверка на выигрыш:
    if count > 4:
        if board[1][1] == board[0][0] == board[2][2]:
            win = True
        elif board[1][1] == board[0][2] == board[2][0]:
            win = True
        elif board[1][1] == board[0][1] == board[2][1]:
            win = True
        elif board[1][1] == board[1][0] == board[1][2]:
            win = True
        elif board[0][0] == board[0][1] == board[0][2]:
            win = True
        elif board[2][0] == board[2][2] == board[2][1]:
            win = True
        elif board[0][0] == board[1][0] == board[2][0]:
            win = True
        elif board[0][2] == board[1][2] == board[2][2]:
            win = True

if win == False:
    print('Ничья')
else:
    if first_player:
        print('Выиграл второй игрок')
    else:
        print('Выиграл первый игрок')
