import os
import time
from person import person

class player(person):
    def __init__(self, obj_board):
        person.__init__(self,2, 36)
        # self.body = [["/","/","/","/","/","/","/","/"],["|"," ","^"," "," ","^"," ","|"],["("," "," ","\'","\'"," "," ",")"],[" "," ","/"," ","\\"," "," "," "],["_","/"," "," "," ","\\","_", " "]]
        self.__body=[["|", "|", "|", "|", "|", "|", "|", "|"], ["|", " ", "@", " ", " ", "@", " ", "|"], ["|", " ", " ", "`", "`", " ", " ", "|"], ["|", " ", " ", "=", "=", " ", " ", "|"], ["|", "W", "W", "W", "W", "W", "W", "|"]]
        # self.__body = [["J","J","J","J","J","J","J","J"],["J","J","J","J","J","J","J", "J"],["J","J","J","J","J","J","J", "J"],["J","J","J","J", "J","J","J","J"],["J","J","J","J","J","J","J", "J"]]
        self.__lives = 10
        self.start = time.time()
        self.time = 100
        self.__coins = 0
        self.__score = 0
        self.bullets = []
        
        person.position(self, 2, 36)
        # for row in self.body:
        #     print(row)
        tempx = 36
        tempy = 2
        for row in self.__body:
            tempy = 2
            for element in row:
                obj_board.set_grid(element, tempx, tempy)
                # place[tempx][tempy] = element
                tempy += 1
            tempx += 1
    def moveup(self,place, obj_board, num):
        # print("current values")
        # print(self._curx)
        # print(self._cury)
        curx = self.curx
        cury = self.cury
        if(curx <=  5):
            return
        if place[curx-1][cury] == 'F' or place[curx-1][cury+1] == 'F' or place[curx-1][cury+2] == 'F' or place[curx-1][cury+3] == 'F' or place[curx-1][cury+4] == 'F'or place[curx-1][cury+5] == 'F' or place[curx-1][cury+6] == 'F' or place[curx-1][cury+7] == 'F' or place[curx-2][cury] == 'F' or place[curx-2][cury+1] == 'F' or place[curx-2][cury+2] == 'F' or place[curx-2][cury+3] == 'F' or place[curx-2][cury+4] == 'F' or place[curx-2][cury+5] == 'F' or place[curx-2][cury+6] == 'F' or place[curx-2][cury+7] == 'F' or place[curx-3][cury] == 'F' or place[curx-3][cury+1] == 'F' or place[curx-3][cury+2] == 'F' or place[curx-3][cury+3] == 'F' or place[curx-3][cury+4] == 'F'or place[curx-3][cury+5] == 'F' or place[curx-3][cury+6] == 'F' or place[curx-3][cury+7] == 'F':
            if place[curx][cury] != 'S':
                self.__lives -= 1 
        elif place[curx-1][cury] == 'M' or place[curx-1][cury+1] == 'M' or place[curx-1][cury+2] == 'M' or place[curx-1][cury+3] == 'M' or place[curx-1][cury+4] == 'M' or place[curx-1][cury+5] == 'M' or place[curx-1][cury+6] == 'M' or place[curx-1][cury+7] == 'M'or  place[curx-2][cury] == 'M' or place[curx-2][cury+1] == 'M' or place[curx-2][cury+2] == 'M' or place[curx-2][cury+3] == 'M' or place[curx-2][cury+4] == 'M' or place[curx-2][cury+5] == 'M' or place[curx-2][cury+6] == 'M' or place[curx-2][cury+7] == 'M' or place[curx-3][cury] == 'M' or place[curx-3][cury+1] == 'M' or place[curx-3][cury+2] == 'M' or place[curx-3][cury+3] == 'M' or place[curx-3][cury+4] == 'M' or place[curx-3][cury+5] == 'M' or place[curx-3][cury+6] == 'M' or place[curx-3][cury+7] == 'M':
            
                return
        else:
            coin=0
            for k in range(0, 5):
                for j in range(0,8):
                    if place[curx+num+k][cury+j] == '$':
                        # print(curx, cury,curx+num+k, cury+j, place[curx+num-k][cury+j], coin)
                        coin += 1
               
            
            self.__coins += coin
            if(curx > 4):
                person.changeposup(self, num, obj_board )
        # print("new values")
        # print(self.curx)
        # print(self.cury)        
    def moveleft(self,place, obj_board, num):
    
        curx = self.curx

        cury = self.cury
        if cury <= 2:
            return
        if place[curx][cury-1] == 'F' or place[curx+1][cury-1] == 'F' or place[curx+2][cury -1] == 'F' or place[curx+3][cury-1] == 'F' or place[curx+4][cury-1] == 'F'or  place[curx][cury-2] == 'F' or place[curx+1][cury-2] == 'F' or place[curx+2][cury -2] == 'F' or place[curx+3][cury-2] == 'F' or place[curx+4][cury-2] == 'F':
            if place[curx][cury] != 'S':
                self.__lives -= 1 
        elif place[curx][cury-1] == 'M' or place[curx+1][cury-1] == 'M' or place[curx+2][cury -1] == 'M' or place[curx+3][cury-1] == 'M' or place[curx+4][cury-1] == 'M'or place[curx][cury-2] == 'M' or place[curx+1][cury-2] == 'M' or place[curx+2][cury -2] == 'M' or place[curx+3][cury-2] == 'M' or place[curx+4][cury-2] == 'M':
            return
        else:
            coin=0
            for k in range(0,8):
                for i in range(0,5):
                    if place[curx+i][cury+num+k] == '$':
                        # print(curx, cury, curx+i, cury+num-k, place[curx+i][cury+num-k], coin)
                        coin += 1
            self.__coins += coin
            person.changeposleft(self, num, 0, obj_board)
        # print("new values")
        # print(self.curx)
        # print(self.cury)
    def moveright(self, place, obj_board, num):
        # print("current values")
        # print(self.curx)
        # print(self.cury)
        curx = self.curx    
        cury = self.cury + 7
        place = place
        if cury >= 298:
            return
        if place[curx][cury+1] == 'F' or place[curx+1][cury+1] == 'F' or place[curx+2][cury +1] == 'F' or place[curx+3][cury+1] == 'F' or place[curx+4][cury+1] == 'F' or place[curx][cury+2] == 'F' or place[curx+1][cury+2] == 'F' or place[curx+2][cury +2] == 'F' or place[curx+3][cury+2] == 'F' or place[curx+4][cury+2] == 'F':
            if place[curx][cury] != 'S':
                self.__lives -= 1
        elif place[curx][cury+1] == 'M' or place[curx+1][cury+1] == 'M' or place[curx+2][cury +1] == 'M' or place[curx+3][cury+1] == 'M' or place[curx+4][cury+1] == 'M'or place[curx][cury+2] == 'M' or place[curx+1][cury+2] == 'M' or place[curx+2][cury +2] == 'M' or place[curx+3][cury+2] == 'M' or place[curx+4][cury+2] == 'M' or place[curx][cury+3] == 'M' or place[curx+1][cury+3] == 'M' or place[curx+2][cury +3] == 'M' or place[curx+3][cury+3] == 'M' or place[curx+4][cury+3] == 'M':
            return
        else:
            coin=0
            for k in range(0,8):
                for i in range(0,5):
                    if place[curx+i][cury+num-k] == '$':
                        # print(curx, cury, curx+i, cury+num+k, place[curx+i][cury+num+k], coin)
                        coin += 1

            self.__coins += coin
        
            person.changeposright(self, num, 0, obj_board)   
    
    def movedown(self, place, obj_board, num):

        # print("current values")
        # print(self.curx)
        # print(self.cury)
        curx = self.curx +4 + num
        cury = self.cury 
        place = place
        
        if place[curx][cury] == 'F' or place[curx][cury+1] == 'F' or place[curx][cury +2] == 'F' or place[curx][cury+3] == 'F' or place[curx][cury+4] == 'F' or place[curx][cury+5] == 'F' or place[curx][cury+6] == 'F' or place[curx][cury+7] == 'F':
            if place[curx-1][cury] != 'S':
                self.__lives -= 1
        elif place[curx][cury] == 'M' or place[curx][cury+1] == 'M' or place[curx][cury +2] == 'M' or place[curx][cury+3] == 'M' or place[curx][cury+4] == 'M' or place[curx][cury+5] == 'M' or place[curx][cury+6] == 'M' or place[curx][cury+7] == 'M':
            return
        else:
            coin=0
            for k in range(0, 5):
                for j in range(0,8):
                    if place[curx+k][cury-j] == '$':
                        print(curx, cury,curx+k, cury+j, place[curx+k][cury+j], coin)
                        coin += 1
            
            self.__coins += coin
        
            person.changeposdown(self, num, obj_board)   
            # print("new values")
            # print(self.curx)
            # print(self.cury)   

    def shoot(self, obj_board):
        starx = self.curx + 2
        stary = self.cury + 10
        self.bullets.append([starx,stary,0])
        obj_board.set_grid('o', starx, stary)
        
    def movebullets(self, place, obj_board, speed):
        for x in self.bullets:
            # for starx in x:
            if x[1] >= 273 or x[1] == 0 or x[2] == 20:
                obj_board.set_grid(' ', x[0], x[1])
                # place[x[0]][x[1]] = ' '
                x[1] = 0
                continue
            obj_board.set_grid(' ', x[0], x[1])
           
            if speed ==1: 
                x[1] += 1
            elif speed == 2:
                x[1] += 2
            obj_board.set_grid('o', x[0], x[1])
            x[2] += 1
            
            
    def checkdamage(self, place, obj_board):
        starx = self.curx
        stary = self.cury
        if place[starx][stary] == 'S':
            for x in range(starx, starx +5):
                for y in range(stary, stary+8):
                    obj_board.set_grid('S', x, y)
                    # place[x][y] =   'S'
            return
        for x in range(starx, starx +5):
            for y in range(stary, stary+8):
                if place[x][y] == 'I' :
                    self.__lives -= 1 
                    obj_board.set_grid(self.__body[x-starx][y-stary], x, y)
                    place[x][y] =   self.__body[x-starx][y-stary]  
                    break
                obj_board.set_grid(self.__body[x-starx][y-stary], x, y)
                # place[x][y] =   self.body[x-starx][y-stary]
                   
    def activateshield(self, obj_board):
        starx = self.curx
        stary = self.cury
        for x in range(starx, starx +5):
            for y in range(stary, stary+8):
                obj_board.set_grid('S', x, y)
                # place[x][y] =  'S'
    
    def deactivateshield(self, obj_board):
        starx = self.curx
        stary = self.cury
        for x in range(starx, starx +5):
            for y in range(stary, stary+8):
                obj_board.set_grid('J', x, y)
                # place[x][y] =  'J'
    
    def set_lives(self, k):
        self.__lives = k
    def get_lives(self):
        return self.__lives

    def set_coins(self, k):
        self.__coins = k
    def get_coins(self):
        return self.__coins

    def set_score(self, k):
        self.__score = k
    def get_score(self):
        return self.__score