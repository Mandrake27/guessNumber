import random

print("Я загадал число от 1 до 100")
print("Попытайся его угадать за наименьшее количество попыток.\n")

number = random.randint(1, 100)
guess = None
difficulty = {
    1: 10,
    2: 5,
    3: 3,
}
difficulty_choose = int(
        input('Выберите уровень сложности, где 1 ур. - 10 попыток, 2 ур. - 5 попыток, 3 ур. - 3 попытки: ')
    )

while difficulty_choose >= 1 or difficulty_choose <= 3:
    if difficulty_choose < 1 or difficulty_choose > 3:
        difficulty_choose = int(
            input('Уровня всего 3, выберите от 1 до 3: ')
        )
    else:
        break

max_tries = difficulty[difficulty_choose]
tries = 0

players = []
number_of_players = int(input('Сколько игроков будет играть?: '))

for player in range(number_of_players):
    if number_of_players > 1:
        name = input(f'Введите имя {player + 1}-го игрока: ')
    else:
        name = input(f'Введите имя игрока: ')
    players.append(name)

winner = False
winner_name = None
while not winner:
    tries += 1
    if tries > max_tries:
        if len(players) > 1:
            print('Все игроки - проиграли(')
        else:
            print('Ты проиграл(')
        break
    print(f'Попытка: {tries}')
    for player in players:
        guess = int(input(f'Давай, {player}, загадывай число: '))
        if guess == number:
            winner = True
            winner_name = player
        elif guess > number:
            print("Меньше...")
        else:
            print("Больше...")

else:
    if tries <= 3:
        print(f"{winner_name}, да ты ас! Я загадал: {number}")
        print(f"И это заняло у тебя всего, {tries} попытки!")
    else:
        print(f"{winner_name}, ты угадал(-а)! Я загадал: {number}")
        print(f"И это заняло у тебя {tries} попыток!\n")

