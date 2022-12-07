# Создайте программу для игры в "Крестики-нолики".

#Функция для рисования доски игры
def draw_board  (board) :
    print ('-------------')
    for i in range(3) :
        print (f'| {board[i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |')
        print ('-------------')

#Функция для ходов
def move (hod) :
    valid = False
    while not valid:
        player_index = int (input (f'Ваш ход, выберите ячейку для {hod}: '))
        if player_index >= 1 and player_index <= 9:
            if (str (board[player_index - 1]) not in 'XO'):
                board[player_index - 1] = hod
                valid = True
            else:
                print('Занято, выберите другую ячейку')
        else:
            print('Введите число от 1 до 9')

#Функция для проверки выигрыша
def victory_check(board) :
    victory = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for i in victory :
        if board[i[0]] == board[i[1]] == board[i[2]] :
            return board[i[0]]
    return False


board = list (range (1, 10))
count = 0
draw_board (board)
while count < 9 :
    if count % 2 == 0 :
        move ('X')
    else:
        move ('O')
    count +=1
    if count > 4 :
        win = victory_check (board)
        if win :
            draw_board (board)
            print (f'{win} Победили!')
            break
        if count == 9 :
            draw_board (board)
            print ('Ничья')
            break
    draw_board (board)