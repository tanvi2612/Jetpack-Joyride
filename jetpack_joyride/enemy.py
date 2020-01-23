from person import person

class enemy(person):
    def __init__(self, obj_board):
        person.__init__(self, 272, 36)
        person.position(self, 272, 36)
        # self.body = [["B", "B", "B", "B", "B", "B", "B", "B"], ["B", "B", "B", "B", "B", "B", "B", "B"], ["B", "B", "B", "B", "B", "B", "B", "B"], ["B", "B", "B", "B", "B", "B", "B", "B"], ["B", "B", "B", "B", "B", "B", "B", "B"]]
        self.body = [["/","/","/","/","/","/","/","/"], ["(", " ", "^", " ", " ", "^", " ", ")"], ["<", " ", " ", "\'", "\'", " ", " ", ">"], [" ", "x", "x", "x", "x", "x", "x", " "], [" ", " ", "x", "x", "x", "x", " ", " "]]
        self.__lives = 15
        tempx = self.curx
        tempy = self.cury
        for row in self.body:
            tempy = self.cury
            for element in row:
                obj_board.set_grid(element, tempx, tempy)
                # obj_board[tempx][tempy] = element
                tempy += 1
            tempx += 1
        self.ice = []

    def set_lives(self, k):
        self.__lives = k
    def get_lives(self):
        return self.__lives
    def moveup(self, obj_board, speed):
        if speed == 1:
            person.changeposup(self, -2, obj_board)
        elif speed == 2:
            person.changeposup(self, -4, obj_board)
        
    def movedown(self, obj_board, speed):
        if speed == 1:
            person.changeposdown(self, 2, obj_board)
        elif speed == 2:
            person.changeposdown(self, 4, obj_board)
    def moveice(self, obj_board, speed):
        for x in self.ice:
            # for starx in x:
            if x[1] <= 200 or x[1] == 0:
                obj_board.set_grid(' ', x[0], x[1])
                # obj_board[x[0]][x[1]] = ' '
                x[1] = 0

                continue
            obj_board.set_grid(' ', x[0], x[1])
            # obj_board[x[0]][x[1]] = ' '
            # obj_board[x[0]+1][x[1]] = ' '
            # obj_board[x[0]][x[1]+1] = ' '
            # obj_board[x[0]+1][x[1]+1] = ' '
            # print(starx, star)
            if speed == 1:
                x[1] -= 2
            elif speed == 2:
                x[1] -= 4
            obj_board.set_grid('I', x[0], x[1])
            # obj_board[x[0]][x[1]] = 'I'
            # obj_board[x[0]+1][x[1]] = 'I'
            # obj_board[x[0]][x[1]+1] = 'I'
            # obj_board[x[0]+1][x[1]+1] = 'I'

    def checkdamage(self, obj_board):
        starx = self.curx
        stary = self.cury
        place = obj_board.get_grid()
        for x in range(starx, starx +5):
            for y in range(stary, stary+8):
                if place[x][y] !=  self.body[x-starx][y-stary]:
                    obj_board.set_grid(self.body[x-starx][y-stary], x, y)
                    # obj_board[x][y] =   self.body[x-starx][y-stary]
                    self.__lives -= 1 
                    break
                obj_board.set_grid(self.body[x-starx][y-stary], x-starx, y-stary)
                # obj_board[x][y] =   self.body[x-starx][y-stary]

    def shootice(self, obj_board):
        starx = self.curx + 2
        stary = self.cury - 6
        self.ice.append([starx,stary])
        obj_board.set_grid('I', starx, stary)
        # obj_board[starx][stary] = 'I'
        # obj_board[starx+1][stary] = 'I'
        # obj_board[starx][stary+1] = 'I'
        # obj_board[starx+1][stary+1] = 'I'