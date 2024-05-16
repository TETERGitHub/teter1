from data import *

def fight(current_enemy0):
    enemy = enemies[current_enemy0]

    while player['hp']>0 and enemy['hp']>0:
       
        player['hp'] -= enemy['attack']
        enemy['hp'] -= enemy['attack']

        print(f'Здоровье игрока = {player["hp"]}')
        print(f'Здоровье врага = {enemy["hp"]}')

        print()
        sleep(1.5)

        if enemy['hp'] <= 0:

            print(f'Противник - {enemy["name"]}: {enemy}')





def info_player():
    print(f'Игрок - {player["name"]}')
    print(f'копеек = {player["money"]}')
    print(f'тело = {player["hp"]}')
    print(f'удар = {player["damage"]}')
    print(f'сильный удар = {player["strong_hit"]}')
    print(f'слабый удар = {player["weak_hit"]}')


def training(training_type):
    pass

