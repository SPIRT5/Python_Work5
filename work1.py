# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота "интеллектом"

import random

#Функция для хода игрока
def player_input (player_name):
    k = int (input (f'{player_name}, введите количество конфет, которое возьмете от 1 до 28: '))
    while k < 1 or k > 28:
        k = int (input (f'{player_name}, введите корректное количество конфет: '))
    return k

#Функция для хода робота
def bot_input (konfet):
    k = random.randrange (1, 29)
    if ((konfet - k) < 58 and konfet > 58) :
        k = konfet - 58
    if (konfet <= 56 and konfet > 29) :
        k = konfet - 29
    if (konfet - k) <= 28 :
        k = random.randrange (1, konfet)
    return k

name1 = input ('Введите имя первого игрока: ')
name2 = input ('Введите имя второго игрока: ')

#Жеребьевка игроков
igrok = random.randrange (1, 3)

if igrok == 1 :
    print (f'Первый ход делает: {name1}')
else :
    print (f'Первый ход делает: {name2}')

konfet = 150
count1 = 0
count2 = 0

while konfet > 28 :
    if igrok == 1 :
        hod = player_input (name1)
        count1 += hod
        konfet -= hod
        igrok = 2
        print(f'Ходил {name1}, он взял {hod}, теперь у него {count1}. Осталось на столе {konfet} конфет.')
    else :
        hod = bot_input (konfet)
        count2 += hod
        konfet -= hod
        igrok = 1
        print(f'Ходил {name2}, он взял {hod}, теперь у него {count2}. Осталось на столе {konfet} конфет.')

if igrok == 1 :
    print(f'Выиграл {name1}')
else:
    print(f'Выиграл {name2}')
