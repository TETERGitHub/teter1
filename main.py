from data import *
from func import *

print('вы играете в игру - пупс бес присмотра')

name = input('введите своё имя,: ')
player['name'] = name

print('ваше имя =', player['name'])
current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой! 
2 - Информация об игроке  
3 - Информация о текущем противнике  //в разработке
4 - Показать инвентарь  //в разработке
5 - Тренировка  //в разработке
6 - Магазин  //в разработке
7 - Получение денег  //в разработке
''')
    if action ==  '1':
        fight(current_enemy)
    
   
    
    
    
    
    
    
    
    
    
    
    
    if action == '2':  
        info_player()
 
if action == '5':  
     training_type = input('1 - тренировать атаку, 2 - тренировать оборону')
     training(training_type)

































