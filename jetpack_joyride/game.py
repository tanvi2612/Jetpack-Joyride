import signal
import os
import time
import subprocess
import random

from obstacles import obstacles, magnet, fire
from board import board, coins
from enemy import enemy
from person import person
from player import player
import inputtext
board_obj = board()
board_obj.setup()
coin = [" " for x in range(0, 100)]
for x in range(0,80):
    coin[x] = coins()
    board_obj.addcoins(coin[x])
bplace = board_obj.get_grid()
firebeam = [" " for x in range(0, 20)]
for rand in range(0, 15):
    firebeam[rand] = fire(board_obj, (rand * 23) %
                          45, (rand*43) % 300, rand % 3)
    # k = rand % 3
    # if k == 0:

magnet_obj = magnet(board_obj)


player_obj = player(board_obj)
enemy_obj = enemy(board_obj)

# os.system('clear')
print(chr(27) + "[2J")
board_obj.showscreen(player_obj.cury - 2)
x = 0
shield = -1
shieldtime = 0
tracktime = 0
shieldstart = -1
board_obj.set_grid('S', 0, 60)
board_obj.set_grid('H', 0, 61)
board_obj.set_grid('I', 0, 62)
board_obj.set_grid('E', 0, 63)
board_obj.set_grid('L', 0, 64)
board_obj.set_grid('D', 0, 65)
# obj_board.set_grid('S', 0, 60)
airtime = 0
speed = 1
flag = 0
while(True):

    gone = round(time.time() - player_obj.start)
    if shield == 1:
        shieldtime = gone - shieldstart
        if shieldtime >= 10:
            player_obj.deactivateshield(board_obj)
            shield = 2
            shieldstart = gone
    elif shield == 2:
        shieldtime = gone - shieldstart
        if shieldtime >= 60:
            shield = -1
            bplace[0][60] = 'S'
            bplace[0][61] = 'H'
            bplace[0][62] = 'I'
            bplace[0][63] = 'E'
            bplace[0][64] = 'L'
            bplace[0][65] = 'D'
            shieldstart = 0
    player_obj.time = 120 - gone
    if enemy_obj.get_lives()  <= 0:
        os.system('clear')

        print("YAY YOU WIN")

        print("Your score:", end=" ")
        print(player_obj.get_coins() + player_obj.time)
        break
    if player_obj.time <= 0:
        os.system('clear')
        print("TIME OVER")
        print("YOU LOSE")
        print("GAME OVER")
        print("Your score:", end=" ")
        print(player_obj.get_coins())
        break
    if(player_obj.get_lives() <= 0):
        os.system('clear')
        print("YOU LOSE")
        print("GAME OVER")
        print("Your score:", end=" ")
        print(player_obj.get_coins())
        break
    player_obj.movebullets(bplace, board_obj, speed)
    enemy_obj.moveice(board_obj,speed)
    player_obj.checkdamage(bplace, board_obj)
    enemy_obj.checkdamage(board_obj)
    for rand in range(0, 15): 
        firebeam[rand].checkcol(board_obj)

    if magnet_obj.get_y() >= player_obj.cury - 2 and magnet_obj.get_y() < player_obj.cury + 80:
        flag = 1
        if magnet_obj.get_x() < player_obj.curx - 4:
            player_obj.moveup(bplace, board_obj, -2)
        if magnet_obj.get_x() > player_obj.curx + 3:
            player_obj.movedown(bplace, board_obj, 1)
        if magnet_obj.get_y() > player_obj.cury + 2:
            player_obj.moveright(bplace, board_obj, 1)
        if magnet_obj.get_y() < player_obj.cury - 2:
            player_obj.moveleft(bplace, board_obj, -2)
    if player_obj.curx != 36 and flag == 0:
        # and time.time()-airtime>1
        airtime += 1
        k = 5 * airtime * airtime
        if player_obj.curx + k >= 36:
            k = 36 - player_obj.curx
        player_obj.movedown(bplace, board_obj, k)
    
    ch = inputtext.get_input()
    flag = 0
    if(ch == 'q'):
        os.system('clear')
        print("GAME OVER")
        break
    elif(ch == 'a'):
        if speed == 1:
            player_obj.moveleft(bplace, board_obj, -3)
        elif speed == 2:
            player_obj.moveleft(bplace, board_obj, -6)
    elif(ch == 'd'):
        if speed == 1:
            player_obj.moveright(bplace, board_obj, 2)
        elif speed == 2:
            player_obj.moveright(bplace, board_obj, 4)
    elif(ch == 'w'):
        # airtime = time.time()
        airtime = 0
        flag = 1
        if speed == 1:
            player_obj.moveup(bplace, board_obj, -3)
        elif speed == 2:
            player_obj.moveup(bplace, board_obj, -5)
    elif(ch == 's'): 

        player_obj.shoot(board_obj)
    elif(ch == 'b'):
        if speed ==1:
            speed = 2
        elif speed == 2:
            speed =1
    elif(ch == ' '):
        if shield == -1:
            player_obj.activateshield(board_obj)
            shield = 1
            shieldstart = gone
            board_obj.set_grid(' ', 0, 60)
            board_obj.set_grid(' ', 0, 61)
            board_obj.set_grid(' ', 0, 62)
            board_obj.set_grid(' ', 0, 63)
            board_obj.set_grid(' ', 0, 64)
            board_obj.set_grid(' ', 0, 65)
            
    if player_obj.cury <= 218:
        if speed == 1:
            player_obj.moveright(bplace, board_obj, 1)
        elif speed == 2:
            player_obj.moveright(bplace, board_obj, 5)
    if player_obj.cury >= 215:
        if enemy_obj.curx > player_obj.curx:
            enemy_obj.moveup(board_obj, speed)
        elif enemy_obj.curx < player_obj.curx:
            enemy_obj.movedown(board_obj, speed)
        if gone % 6 == 0:
            enemy_obj.shootice(board_obj)
    board_obj.set_grid(player_obj.get_lives(), 0, 6)
    board_obj.set_grid(player_obj.get_coins(), 0, 14)
    board_obj.set_grid(player_obj.get_coins(), 0, 24)
    board_obj.set_grid(player_obj.time, 0, 31)
    board_obj.set_grid(enemy_obj.get_lives(), 0, 46)
    # board_obj.set_grid('D', 0, 65)
    # bplace[0][6] = player_obj.lives
    # bplace[0][14] = player_obj.coins
    # bplace[0][24] = player_obj.coins
    # bplace[0][31] = player_obj.time
    # bplace[0][46] = enemy_obj.lives

    board_obj.showscreen(player_obj.cury - 2)
