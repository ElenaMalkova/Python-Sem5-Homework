# Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? a) Добавьте игру против бота b) Подумайте как наделить бота "интеллектом"

# Игра человека против человека

# Ввод имен игроков и жеребьевка
import random
print("Введите имя первого игрока: ")
player_x = input()
x_number = random.randint(1, 10)
print(f"{player_x}, ваше число для жеребьевки: {x_number}")

print("Введите имя второго игрока: ")
player_y = input()
y_number = random.randint(1, 10)
if y_number == x_number:
    y_number = random.randint(1, 10)
    print(f"{player_y}, ваше число для жеребьевки: {y_number}")
else:
    print(f"{player_y}, ваше число для жеребьевки: {y_number}")

print("Результат жеребьевки: ")

if x_number > y_number:
        first = player_x
        second = player_y
        print(f"{player_x}, вы - игрок 1, {player_y}, вы - игрок 2")
else:
        print(f"{player_y}, вы - игрок 1, {player_x}, вы - игрок 2")
        first = player_y
        second = player_x
    
# Игра
candies = 80
moves = range(1, 10000)
print(f"Начнем игру! На столе лежит {candies} конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")
for i in moves:
    if i%2 != 0:
        print(f"Ходит {first}")
        print(f"Сколько конфет из {candies} ты возьмешь?: ")
        num = int(input())
        if 0 > num or num > 28 or num > candies:
            print("Ввод некорректный, пропускаешь ход")
        else: 
            candies -= num
            if candies <= 0:
                break
    else:
        print(f"Ходит {second}")
        print(f"Сколько конфет из {candies} ты возьмешь?: ")
        num = int(input())
        if 0 > num or num > 28 or num > candies:
            print("Ввод некорректный, пропускаешь ход")
        else: 
            candies -= num
            if candies <= 0:
                break
winner = i

if winner % 2 == 0:
    print(f"Победитель - {second}!")
else:
    print(f"Победитель - {first}!")