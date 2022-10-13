# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def zadacha_abc():
    text = str(input('Введите текст: '))
    trigger = 'абв'
    text = text.split()
    result = []

    for i in range(len(text) - 1):
        if trigger not in text[i]:
            result.append(text[i])

    result = " ".join(result)
    print(result)

# zadacha_abc()

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

candy = int(input('Сколько конфет лежит на столе? '))
candy_count = int(input('Сколько конфет можно брать за 1 ход? '))

def first_play_win(candy, candy_count): #Код-эксперимент, на нем отрабатывал правильную работу алгоритма по подсчету конфет
    import random
    while candy > 0:
        if candy < candy_count:
            player_first_move = candy
        else:
            player_first_move = (candy % candy_count + 1)
        candy = candy - player_first_move
        if candy == 0: 
            print('Выиграл игрок, ходивший первым!')
            break
        player_loser = random.randrange(1, candy_count + 1)
        candy = candy - player_loser
        if candy == 0: 
            print('Выиграл игрок, ходивший вторым! Ха-ха, мы же знаем что этого никогда не произойдёт')

def candy_game(): # Игра для двух человек.

    candy = int(input('Сколько конфет лежит на столе? '))
    candy_count = int(input('Сколько конфет можно брать за 1 ход? '))

    while candy > 0:
        player_first_move = math_candy(candy, candy_count)
        candy = candy - player_first_move
        print(f'Осталось {candy} конфет')
        if candy == 0: 
            print('Выиграл игрок, ходивший первым!')
            break
        player_loser = math_candy(candy, candy_count)
        candy = candy - player_loser
        print(f'Осталось {candy} конфет')
        if candy == 0: 
            print('Выиграл игрок, ходивший вторым!')
        if candy < 0:
            candy = 0
            print('Мы попали в реальность, в которой конфеты могут принимать отрицательное значение. Сворачиваемся, нас развоплотили!')

def candy_game_with_bot(): # Игра с ботом

    candy = int(input('Сколько конфет лежит на столе? '))
    candy_count = int(input('Сколько конфет можно брать за 1 ход? '))
    lot = fate()
    if lot == 0:
        while candy > 0:
            player_first_move = bot_brain(candy, candy_count)
            candy = candy - player_first_move
            print(f'Количество конфет, которые взял бот: {player_first_move}. Осталось {candy}')
            if candy == 0: 
                print('Выиграл бот, а ты чего ждал?')
                break
            player_loser = math_candy(candy, candy_count)
            candy = candy - player_loser
            print(f'Осталось {candy} конфет')
            if candy == 0: 
                print('Ты выиграл! Как это вообще получилось?!')
            if candy < 0:
                candy = 0
                print('Мы попали в реальность, в которой конфеты могут принимать отрицательное значение. Сворачиваемся, нас развоплотили!')
    else:
        while candy > 0:
            player_first_move = math_candy(candy, candy_count)
            candy = candy - player_first_move
            print(f'Осталось {candy} конфет')
            if candy == 0: 
                print('Ты выиграл! Как это вообще получилось?!')
                break
            player_loser = bot_brain(candy, candy_count)
            candy = candy - player_loser
            print(f'Количество конфет, которые взял бот: {player_loser}. Осталось {candy}')
            if candy == 0: 
                print('Выиграл бот, а ты чего ждал?')
            if candy < 0:
                candy = 0
                print('Мы попали в реальность, в которой конфеты могут принимать отрицательное значение. Сворачиваемся, нас развоплотили!')
        
def math_candy(candy, candy_count):
    player = int(input('Сколько берёшь конфет? '))
    if player > candy_count or player < 1:
        print(f'Жульничать нехорошо! Укажи корректно сколько берешь конфет! От 1 до {candy_count}: ')
        player = math_candy(candy, candy_count)
    return player

def fate(): # Метод для определения того кто ходит первым
    import random
    choise = int(input('Орёл или решка? Хотя, раз уж мы программисты и "бросать монетку" будет код, то спрошу иначе. Истина или ложь? Ответ пиши цифрой - ноль или единицу: '))
    fate = random.randrange(0, 2)
    if fate == choise:
        print('Угадал! Ходишь первый. Удачи!')
        return 1
    else:
        print('Не угадал. Бот ходит первым. И ты знаешь что теперь с тобой будет')
        return 0

def bot_brain(candy, candy_count): # Тут я подумал как наделить бота интеллектом
    import random
    if candy < candy_count:
        player = candy
    if (candy % (candy_count + 1)) > 0:
        player = (candy % (candy_count + 1))
    else:
        player = random.randrange(1, candy_count + 1)
    return player

# candy_game()
# candy_game_with_bot():

# 3. Создайте программу для игры в ""Крестики-нолики"".

import math

def fill_square(matrix):
    for i in range (0, len(matrix), 3):
        print(f" {matrix[i]} {matrix[i+1]} {matrix[i+2]} ")

def change_players(player):
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player

def move(player, field):
    point = input(f"В поле с каким номером ставишь {player}? ")
    if point.isdigit():
        if 0 < int(point) < 10:
            point = int(point) - 1
            if field[point] != "X" and field[point] != "O":
                return point
            else:
                print("Указанное поле занаято.")
                return move(player, field)
        else:
            print("Такого поля не существует")
            move(player, field)
    else:
        print("Введите поле цифрой от 1 до 9")
        move(player, field)

def x_o_game():
    import math
    field = []
    for i in range (0,9):
        field.append(i+1)

    player = "X"
    fill_square(field)
    win = False
    for i in range(9):
        point = move(player, field)
        field[int(point)] = player
        fill_square(field)
        player = change_players(player)

#x_o_game()

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def zadacha_rle():
    iffer = int(input('Если нужно кодировать текст - введите 1. Для раскодирования - что-нибудь более оригинальное. '))
    text = str(input('Введите текст: '))
    if iffer == 1:
        result = rle_in(text)
    else:
        result = rle_out(text)
    print(result)

def rle_in(text): 
    encoding = ''
    prev_char = ''
    count = 1

    if not text: return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                encoding = encoding + str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count = count + 1
    else:
        encoding = encoding + str(count) + prev_char
        return encoding

def rle_out(text): 
    decode = '' 
    count = '' 
    for char in text: 
        if char.isdigit(): 
            count = count + char 
        else: 
            decode = decode + char * int(count) 
            count = '' 
    return decode

#zadacha_rle()