import os
import random
from player import player

class coins:
    def __init__(self):
        self.__x = random.randrange(4, 40)
        self.__y = random.randrange(4, 270)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class board:

    def __init__(self):
        self.__rows = 45
        self.__columns = 300
        self.__grid = [[" " for y in range(self.__columns)]
        for x in range(self.__rows)]

    def setup(self):
        for x in range(self.__rows-4, self.__rows):
            for y in range(self.__columns):
                self.__grid[x][y] = "_"
        for x in range(1, 2):
            for y in range(self.__columns):
                self.__grid[x][y] = "\\"
        for y in range(self.__columns):
            self.__grid[2][y] = "_"
        for y in range(self.__rows):
            self.__grid[y][0] = "*"        
            self.__grid[y][self.__columns-1] = "*"
        
    
    def get_grid(self):
        return self.__grid

    def set_grid(self, val, i, j):
        self.__grid[i][j] = val
    
    def addcoins(self, obj_coin):

        self.__grid[obj_coin.get_x()][obj_coin.get_y()] = '$'
        # for k in range(6, 300, 50):
        #     for i in range(4,6):
        #         for j in range(k, k+4):
        #             self.__grid[i][j] = 'O'
        
        # for k in range(15, 300, 60):
        #     for i in range(20,25):
        #         for j in range(k, k+2):
        #             self.__grid[i][j] = 'O'
        
        # for k in range(29, 300, 80):
        #     i = 27
        #     for j in range(k, k+4):
        #         self.__grid[i][j] = 'O'
        #         i += 1

    def showscreen(self, star):
        self.__grid[0][0] = 'L'
        self.__grid[0][1] = 'I'
        self.__grid[0][2] = 'V'
        self.__grid[0][3] = 'E'
        self.__grid[0][4] = 'S'
        self.__grid[0][5] = '='
        
        self.__grid[0][7] = ' '
        
        self.__grid[0][8] = 'C'
        self.__grid[0][9] = 'O'
        self.__grid[0][10] = 'I'
        self.__grid[0][11] = 'N'
        self.__grid[0][12] = 'S'
        self.__grid[0][13] = '='
        # self.__grid[0][14] = ' '
        self.__grid[0][15] = ' '
        self.__grid[0][16] = ' ' 
        self.__grid[0][17] = 'S'
        self.__grid[0][18] = 'C'
        self.__grid[0][19] = 'O'
        self.__grid[0][20] = 'R'
        self.__grid[0][21] = 'E'
        self.__grid[0][22] = '='
        # self.__grid[0][24] = ' '
        self.__grid[0][25] = ' '
        self.__grid[0][26] = 'T'
        self.__grid[0][27] = 'I'
        self.__grid[0][28] = 'M'
        self.__grid[0][29] = 'E'
        self.__grid[0][30] = '='
        self.__grid[0][32] = ' '
        self.__grid[0][33] = 'E'
        self.__grid[0][34] = 'N'
        self.__grid[0][35] = 'E'
        self.__grid[0][36] = 'M'
        self.__grid[0][37] = 'Y'
        self.__grid[0][38] = ' '
        self.__grid[0][39] = 'L'
        self.__grid[0][40] = 'I'
        self.__grid[0][41] = 'V'
        self.__grid[0][42] = 'E'
        self.__grid[0][43] = 'S'
        self.__grid[0][44] = '='
        # os.system('clear')
        
        print('\033c')
        for j in range(70):
            print(self.__grid[0][j], end = ' ')
        print()
        for i in range(1,self.__rows):
            # print(i, end = ' ')
            if star + 80 >= 300:
                star = 220 
                
            for j in range(star, star+80):
                if j >= 300:
                    break
                if self.__grid[i][j] == '$':
                    print("\033[1;93m" + self.__grid[i][j], end = ' ')
                elif self.__grid[i][j] == 'o':
                    print("\033[1;30;40m"+self.__grid[i][j], end = ' ')
                elif self.__grid[i][j] == '\\':
                    print("\033[94m" + self.__grid[i][j], end = ' ')
                elif self.__grid[i][j] == 'F':
                    print("\033[1;31m" +self.__grid[i][j], end = ' ')
                elif self.__grid[i][j] == 'M':
                    print("\033[1;31;40m"+ self.__grid[i][j], end = ' ')
                elif self.__grid[i][j] == '_':
                    print("\033[1;32m" + self.__grid[i][j], end = ' ')
                elif self.__grid[i][j] == 'I':
                    print("\033[1;34m" + self.__grid[i][j], end = ' ')
                elif self.__grid[i][j] == '/' or self.__grid[i][j] == '|' or self.__grid[i][j] == '(' or self.__grid[i][j] == ')' or self.__grid[i][j] == '^' or self.__grid[i][j] == 'x' or self.__grid[i][j] == '\'' or self.__grid[i][j] == '<' or self.__grid[i][j] == '>':
                    print("\033[1;35m" + self.__grid[i][j], end = ' ')
                elif self.__grid[i][j] == '|' or self.__grid[i][j] == '@' or self.__grid[i][j] == '`' or self.__grid[i][j] == '=' or self.__grid[i][j] == 'W':
                    print("\033[1;35m" + self.__grid[i][j], end = ' ')
                elif self.__grid[i][j] == 'S':
                    print("\033[1;36m" + self.__grid[i][j], end = ' ')
                else :
                    print("\033[0m" +self.__grid[i][j], end = ' ')
            print()
        
        # for j in range(star, star+80):
        #     if j > 300:
        #         return
        #     print("\033[0m", j, end = '')
        # print()
