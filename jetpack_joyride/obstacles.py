from player import player
from board import board

class obstacles:
    def __init__(self, x, y):
        if x < 4:
            x = 4
        if x>40:
            x = 40
        if y< 5:
            y =5
        if y>190:
            y = 190
        self._x = x
        self._y = y
        self._dir = -1
        
class magnet(obstacles):
    def __init__(self, obj_board):
        obstacles.__init__(self, 15, 100)
        # for x in range(15,18):
            # for y in range(100,103):
        obj_board.set_grid('M', 15, 100)
        # obj_board[15][100] = 'M'
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
class fire(obstacles):
    def __init__(self,obj_board, x, y, s):
        obstacles.__init__(self, x, y)
        print(self._x, self._y, self._dir, s)
        if(s == 0):
            self.setvert(obj_board, x, y)
        elif(s ==1):
            self.sethori(obj_board, x,y)
        elif(s==2):
            self.setdia(obj_board, x,y)
    def setvert(self, obj_board, x, y):
        if x < 4:
            x = 4
        if x>40:
            x = 40
        if y< 5:
            y =5
        if y>190:
            y = 190
        for i in range(x, x+3):
            for j in range(y, y+2):
                obj_board.set_grid('F', i, j)
                # obj_board[i][j] = 'F'
        self._dir = 1

    def sethori(self, obj_board, x, y):
        if x < 4:
            x = 4
        if x>40:
            x = 40
        if y< 5:
            y =5
        if y>190:
            y = 190
        for i in range(x, x+2):
            for j in range(y, y+3):
                obj_board.set_grid('F', i, j)
                # obj_board[i][j] = 'F'
        self._dir = 2
    def setdia(self, obj_board, x, y):
        self._dir = 3
        if x < 4:
            x = 4
        if x>40:
            x = 40
        if y< 5:
            y =5
        if y>190:
            y = 190
        for i in range(x, x+3):
            for j in range(y, y+2):
                obj_board.set_grid('F', i, j)
                # obj_board[i][j] = 'F'
            y = y +1;
        

    def checkcol(self, obj_board):
        place = obj_board.get_grid()
        x = self._x
        y = self._y
        
        if self._dir == 1:
            flag = 0
            for i in range(x, x+3):
                for j in range(y, y+2):
                    if place[i][j] != 'F':
                        flag = 1
                        break;
            if flag == 1:
                for i in range(x, x+3):
                    for j in range(y, y+2):
                        obj_board.set_grid(' ', i, j)
            return

        elif self._dir == 2:
            flag = 0
            for i in range(x, x+2):
                for j in range(y, y+3):
                    if place[i][j] != 'F':
                        flag = 1
                        break;
            if flag == 1:
                for i in range(x, x+2):
                    for j in range(y, y+3):
                        obj_board.set_grid(' ', i, j)
            return

        elif self._dir == 3:
            flag = 0
            for i in range(x, x+3):
                for j in range(y, y+2):
                    if place[i][j] == 'o':
                        flag = 1
                        break
                y = y+1
            if flag == 1:
                for i in range(x, x+3):
                    for j in range(y, y+2):
                        obj_board.set_grid(' ', i, j)
                    y = y + 1
            return