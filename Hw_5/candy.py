# Создайте программу для игры с конфетами:
#  1. человек против человека
# 2. человек против бота
# 3. человек против бота с интеллектом

from random import randint

candies_left = 2021
candies_taken = 0
level = 1

def start_game():
    print('На столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет.\nКто сделает последний ход и оставит на столе 0 конфет, тот победил')
    var = int(input('Выберите вариант игры:\n1.Человек против человека\n2.Человек против бота\nВведите число: '))
    while var < 1 or var > 2:
        var = int(input('Вы ввели неправильное число. Попробуйте еще раз\nВыберите вариант игры:\n1.Человек против человека\n2.Человек против бота\nВведите число: '))
    choose_player(var)

def choose_player(variant):
    global level
    "Функция рандомно выбирает, кто будет ходить первым"
    num = randint(1,2)

    if variant == 1:
        if num == 1:
            first_player_turn()
        else:
            second_player_turn()
        
    if variant == 2:
        level = int(input('Выберите сложность игры:\n1.простая\n2.сложная\nВведите число: '))
        while level < 1 or level > 2:
            print('Вы ввели неправильное число. Попробуйте еще раз\nВыберите сложность игры:\n1.простая\n2.сложная\nВведите число: ')
        if num == 1:
            player_move()
        else:
            bot_move(level)

def player_move():
    global candies_left
    global candies_taken
    global level

    candies_taken = int(input(f'Ваш ход. Осталось {candies_left} конфет. Возьмите количество конфет от 1 до 28: '))
    while candies_taken < 0 or candies_taken > 28 or candies_taken > candies_left:
        candies_taken = int(input(f'Вы ввели неправильное число. Осталось {candies_left} конфет. Попробуйте еще раз: '))
    candies_left -= candies_taken  
    print(f'Вы взяли {candies_taken} конфет. Осталось {candies_left} конфет.')    
    
    if candies_left == 0:
        print('Вы победили')        
    else:
        bot_move(level)

def bot_move(lvl):
    global candies_left
    global candies_taken
    if lvl == 1:
        if candies_left >= 28:
            candies_taken = randint(1, 28)
        else:
            candies_taken = randint(1, candies_left)
        candies_left -= candies_taken
        print(f'Ход бота. Бот взял {candies_taken} конфет')
        
    if lvl == 2:
        if candies_left > 28:
            candies_taken = candies_left % 29
        else:
            candies_taken = candies_left
        candies_left -= candies_taken
        print(f'Ход бота. Бот взял {candies_taken} конфет')
    
    if candies_left == 0:
        print('Бот победил :(')        
    else:
        player_move()

def first_player_turn():
    global candies_left
    global candies_taken
    candies_taken = int(input(f'Ход первого игрока. Осталось {candies_left} конфет. Возьмите количество конфет от 1 до 28: '))
    while candies_taken < 0 or candies_taken > 28 or candies_taken > candies_left:
        candies_taken = int(input(f'Вы ввели неправильное число. Осталось {candies_left} конфет. Попробуйте еще раз: '))
    candies_left -= candies_taken  
    print(f'Вы взяли {candies_taken} конфет.')    
    if candies_left == 0:
        print('Победил первый игрок')        
    else:
        second_player_turn()

def second_player_turn():
    global candies_left
    global candies_taken
    candies_taken = int(input(f'Ход второго игрока. Осталось {candies_left} конфет. Возьмите количество конфет от 1 до 28: '))
    while candies_taken < 0 or candies_taken > 28 or candies_taken > candies_left:
        candies_taken = int(input(f'Вы ввели неправильное число. Осталось {candies_left} конфет. Попробуйте еще раз: '))
    candies_left -= candies_taken  
    print(f'Вы взяли {candies_taken} конфет.')    
    if candies_left == 0:
        print('Победил второй игрок')        
    else:
        first_player_turn()

start_game()