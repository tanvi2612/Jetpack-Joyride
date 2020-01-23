class person:
    def __init__(self, y, x):
        self.x = x
        self.y = y

    def position(self, y, x):
        self.curx = x
        self.cury = y
    
    def changeposleft(self, hor, ver, obj_board):
        
        currx = self.curx
        curry = self.cury
        # print(currx, curry)
        for x in range(currx,currx+5):
            for y in range(curry,curry+8):
                # print(x, y, obj_board[x][y])
                place = obj_board.get_grid()
                obj_board.set_grid(place[x][y], x+ver, y+hor)
                obj_board.set_grid(' ', x, y)
                
                # print(x+ver, y+hor, obj_board[x+ver][y+hor])
        self.curx = currx+ver
        self.cury = curry+hor
        # for i in range(50):
        #     for j in range(80):
        #         print(obj_board[i][j], end = ' ')
        #     print()
        
    def changeposright(self, hor, ver, obj_board):
        
        currx = self.curx
        curry = self.cury
        # print(0, currx, curry)
        for x in range(currx+4,currx-1,-1):
            for y in range(curry+7,curry-1,-1):
                # print(x, y, obj_board[x][y])
                place = obj_board.get_grid()
                obj_board.set_grid(place[x][y], x+ver, y+hor)
                obj_board.set_grid(' ', x, y)
                # print(x+ver, y+hor, obj_board[x+ver][y+hor])
        self.curx = currx+ver
        self.cury = curry+hor
        # for i in range(50):
        #     for j in range(80):
        #         print(obj_board[i][j], end = ' ')
        #     print()
    def changeposdown(self, ver, obj_board):
        
        currx = self.curx
        curry = self.cury
        # print(0, currx, curry)
        for x in range(currx+4,currx-1,-1):
            for y in range(curry+7,curry-1,-1):
                # print(x, y, obj_board[x][y])
                place = obj_board.get_grid()
                obj_board.set_grid(place[x][y], x+ver, y)
                obj_board.set_grid(' ', x, y)
                # print(x+ver, y+hor, obj_board[x+ver][y+hor])
        self.curx = currx+ver
        self.cury = curry
        # for i in range(50):
        #     for j in range(80):
        #         print(obj_board[i][j], end = ' ')
        #     print()
    def changeposup(self, ver, obj_board):
        
        currx = self.curx
        curry = self.cury
        # print(currx, curry)
        for x in range(currx,currx+5):
            for y in range(curry,curry+8):
                # print(x, y, obj_board[x][y])
                place = obj_board.get_grid()
                obj_board.set_grid(place[x][y], x+ver, y)
                obj_board.set_grid(' ', x, y)
                # print(x+ver, y+hor, obj_board[x+ver][y+hor])
        self.curx = currx+ver
        self.cury = curry
        # for i in range(50):
        #     for j in range(80):
        #         print(obj_board[i][j], end = ' ')
        #     print()
        