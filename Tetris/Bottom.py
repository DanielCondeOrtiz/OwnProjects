import Piece
import copy



class Bottom:
    def __init__(self):
        self.current = []
        self.x_left=187
        self.y_top=94
        self.y_bottom = 385
        self.x_right = 315
        self.size = 13
        self.columns = 11

        self.last_silu = None

    def set_columns(self,columns):
        self.columns = columns

    def add(self, object):
        self.current.append(object)

    def get_all(self):
        return self.current

    def get_top_line(self):
        top_line = []

        for i in range(0,self.columns):
            x = self.x_left + 14*i
            y = self.y_bottom

            if len(self.current) > 0:
                for item in self.current:
                    for square in item.pos:
                        if square[0] == x and square[1] < y:
                            y = square[1]

            top_line.append([x,y])

        return top_line

    def check_col(self, pos):
        colision = False

        if len(self.current) > 0:
            for item in self.current:
                for itemsquare in item.pos:
                    if itemsquare[2] == 0:
                        for square in pos:
                            if square[0] == itemsquare[0] and square[1] == itemsquare[1]:
                                return True

        return colision

    def check_next(self, pos):
        colision = False

        if len(self.current) > 0:
            for item in self.current:
                for itemsquare in item.pos:
                    if itemsquare[2] == 0:
                        for square in pos:
                            if square[0] == itemsquare[0] and square[1] + 14 == itemsquare[1]:
                                return True

        return colision

    def finish(self):
        finish = False

        if len(self.current) > 0:
            for item in self.current:
                for itemsquare in item.pos:
                        if itemsquare[1] <= self.y_top:
                            return True

        return finish

    def check_lines(self):
        total_lines = 0

        for j in range(0,23):
            y = self.y_top + 14*j
            line = 0

            for i in range(0,self.columns):
                x = self.x_left + 14*i
                found = False

                for item in self.current:
                    for itemsquare in item.pos:
                        if itemsquare[0] == x and itemsquare[1] == y and itemsquare[2] == 0:
                            found = True
                            line += 1
                            break
                    if found:
                        break

                if not found:
                    break

            if line == self.columns:
                total_lines += 1
                for item in self.current:
                    for itemsquare in item.pos:
                        if itemsquare[1] == y:
                            itemsquare[2] = 1

                        elif itemsquare[1] < y:
                            itemsquare[1] +=14

        list = []
        for item in self.current:
            count = 0
            for itemsquare in item.pos:
                if itemsquare[2] == 1:
                    count += 1

            if count == 4:
                list.append(item)

        for item in list:
            self.current.remove(item)

        list = None

        return total_lines

    def silu(self, object,move,rotate):

        if self.last_silu == None or move != 0 or rotate:
            self.last_silu = copy.deepcopy(object)

            while self.last_silu.pos[0][1] +5 < self.y_bottom and self.last_silu.pos[1][1] +5 < self.y_bottom and self.last_silu.pos[2][1] +5 < self.y_bottom and self.last_silu.pos[3][1] +5 < self.y_bottom and not self.check_next(self.last_silu.pos):
                for i in range(0,4):
                    self.last_silu.pos[i][1] += 14

        return self.last_silu

    def clear():
        self.current = []
