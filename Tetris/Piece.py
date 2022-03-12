from random import randint
from Bottom import Bottom
import copy

class Piece:
    def __init__(self,columns):

        self.x_left=187
        self.y_top=94
        self.y_bottom = 385
        self.x_right = 315
        self.size = 13
        self.columns = columns

        self.pos = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
        self.type = randint(1,7)

        self.moved_down = False

        self.color = [255,255,255]

        #T
        if self.type == 1:
            self.color = [255,255,0]
            self.pos = [[257 + (round((self.columns -11)/2)*14),94,0],[271 + (round((self.columns -11)/2)*14),94,0],[243 + (round((self.columns -11)/2)*14),94,0],[257 + (round((self.columns -11)/2)*14),108,0]]
        #L
        elif self.type == 2:
            self.color = [0,255,0]
            self.pos =[[271 + (round((self.columns -11)/2)*14),108,0],[271 + (round((self.columns -11)/2)*14),94,0],[243 + (round((self.columns -11)/2)*14),108,0],[257 + (round((self.columns -11)/2)*14),108,0]]
        #J
        elif self.type == 3:
            self.color = [255,0,0]
            self.pos =[[243 + (round((self.columns -11)/2)*14),108,0],[243 + (round((self.columns -11)/2)*14),94,0],[271 + (round((self.columns -11)/2)*14),108,0],[257 + (round((self.columns -11)/2)*14),108,0]]
        #I
        elif self.type == 4:
            self.color = [0,0,255]
            self.pos =[[257 + (round((self.columns -11)/2)*14),94,0],[271 + (round((self.columns -11)/2)*14),94,0],[243 + (round((self.columns -11)/2)*14),94,0],[285 + (round((self.columns -11)/2)*14),94,0]]
        ##
        elif self.type == 5:
            self.color = [255,0,255]
            self.pos =[[257 + (round((self.columns -11)/2)*14),94,0],[243 + (round((self.columns -11)/2)*14),108,0],[243 + (round((self.columns -11)/2)*14),94,0],[257 + (round((self.columns -11)/2)*14),108,0]]
        #S
        elif self.type == 6:
            self.color = [0,255,255]
            self.pos =[[257 + (round((self.columns -11)/2)*14),108,0],[257 + (round((self.columns -11)/2)*14),94,0],[243 + (round((self.columns -11)/2)*14),108,0],[271 + (round((self.columns -11)/2)*14),94,0]]
        #Z
        else:
            self.pos =[[257 + (round((self.columns -11)/2)*14),108,0],[257 + (round((self.columns -11)/2)*14),94,0],[271 + (round((self.columns -11)/2)*14),108,0],[243 + (round((self.columns -11)/2)*14),94,0]]


    def get_pos(self):
        return self.pos


    def move(self,move,count,bottom):
        done = False


        if count % 25 == 0 and self.pos[0][1] < self.y_bottom and self.pos[1][1] < self.y_bottom and self.pos[2][1] < self.y_bottom and self.pos[3][1] < self.y_bottom:

            if not self.moved_down:
                for i in range(0,4):
                    self.pos[i][1] += 14


        if count % 8 == 0 and self.moved_down:
            self.moved_down = False

        if count % 2 == 0 and move != 0:
            if move == 1:
                #drop
                while self.pos[0][1] +5 < self.y_bottom and self.pos[1][1] +5 < self.y_bottom and self.pos[2][1] +5 < self.y_bottom and self.pos[3][1] +5 < self.y_bottom and not bottom.check_next(self.pos):
                    for i in range(0,4):
                        self.pos[i][1] += 14

            elif move == 2 and self.pos[0][1] < self.y_bottom and self.pos[1][1] < self.y_bottom and self.pos[2][1] < self.y_bottom and self.pos[3][1] < self.y_bottom:
                #down
                self.moved_down = True
                for i in range(0,4):
                    self.pos[i][1] += 14

            elif move == 3 and self.pos[0][0] > self.x_left and self.pos[1][0] > self.x_left and self.pos[2][0] > self.x_left and self.pos[3][0] > self.x_left:
                #left
                for i in range(0,4):
                    self.pos[i][0] -= 14

                if bottom.check_col(self.pos):
                    for i in range(0,4):
                        self.pos[i][0] += 14

            elif move == 4 and self.pos[0][0] < self.x_right + 14*(self.columns-11) and self.pos[1][0] < self.x_right + 14*(self.columns-11) and self.pos[2][0] < self.x_right + 14*(self.columns-11) and self.pos[3][0] < self.x_right + 14*(self.columns-11):
                #right
                for i in range(0,4):
                    self.pos[i][0] += 14

                if bottom.check_col(self.pos):
                    for i in range(0,4):
                        self.pos[i][0] -= 14


        if self.pos[0][1] +5 > self.y_bottom or self.pos[1][1] +5 > self.y_bottom or self.pos[2][1] +5 > self.y_bottom or self.pos[3][1] +5 > self.y_bottom or bottom.check_next(self.pos):
            done = True

        return done


    def rotate(self):
        #T
        if self.type == 1:

            for i in range (1,4):
                if self.pos[i][0] == self.pos[0][0] - 14 and self.pos[i][1] == self.pos[0][1]:
                    self.pos[i][0] = self.pos[0][0]
                    self.pos[i][1] = self.pos[0][1] -14

                elif self.pos[i][0] == self.pos[0][0] + 14 and self.pos[i][1] == self.pos[0][1]:
                    self.pos[i][0] = self.pos[0][0]
                    self.pos[i][1] = self.pos[0][1] +14

                elif self.pos[i][0] == self.pos[0][0] and self.pos[i][1] == self.pos[0][1] -14:
                    self.pos[i][0] = self.pos[0][0] +14
                    self.pos[i][1] = self.pos[0][1]

                elif self.pos[i][0] == self.pos[0][0] and self.pos[i][1] == self.pos[0][1] +14:
                    self.pos[i][0] = self.pos[0][0] -14
                    self.pos[i][1] = self.pos[0][1]

        #LJ
        elif self.type == 2 or self.type == 3 or self.type == 4:

            for i in range (1,4):
                if self.pos[i][0] == self.pos[0][0] - 14 and self.pos[i][1] == self.pos[0][1]:
                    self.pos[i][0] = self.pos[0][0]
                    self.pos[i][1] = self.pos[0][1] -14

                elif self.pos[i][0] == self.pos[0][0] + 14 and self.pos[i][1] == self.pos[0][1]:
                    self.pos[i][0] = self.pos[0][0]
                    self.pos[i][1] = self.pos[0][1] +14

                elif self.pos[i][0] == self.pos[0][0] and self.pos[i][1] == self.pos[0][1] -14:
                    self.pos[i][0] = self.pos[0][0] +14
                    self.pos[i][1] = self.pos[0][1]

                elif self.pos[i][0] == self.pos[0][0] and self.pos[i][1] == self.pos[0][1] +14:
                    self.pos[i][0] = self.pos[0][0] -14
                    self.pos[i][1] = self.pos[0][1]

                elif self.pos[i][0] == self.pos[0][0] - 28 and self.pos[i][1] == self.pos[0][1]:
                    self.pos[i][0] = self.pos[0][0]
                    self.pos[i][1] = self.pos[0][1] -28

                elif self.pos[i][0] == self.pos[0][0] + 28 and self.pos[i][1] == self.pos[0][1]:
                    self.pos[i][0] = self.pos[0][0]
                    self.pos[i][1] = self.pos[0][1] +28

                elif self.pos[i][0] == self.pos[0][0] and self.pos[i][1] == self.pos[0][1] -28:
                    self.pos[i][0] = self.pos[0][0] +28
                    self.pos[i][1] = self.pos[0][1]

                elif self.pos[i][0] == self.pos[0][0] and self.pos[i][1] == self.pos[0][1] +28:
                    self.pos[i][0] = self.pos[0][0] -28
                    self.pos[i][1] = self.pos[0][1]

        #SZ
        elif self.type == 6 or self.type == 7:

            for i in range (1,4):
                if self.pos[i][0] == self.pos[0][0] - 14 and self.pos[i][1] == self.pos[0][1]:
                    self.pos[i][0] = self.pos[0][0]
                    self.pos[i][1] = self.pos[0][1] -14

                elif self.pos[i][0] == self.pos[0][0] + 14 and self.pos[i][1] == self.pos[0][1]:
                    self.pos[i][0] = self.pos[0][0]
                    self.pos[i][1] = self.pos[0][1] +14

                elif self.pos[i][0] == self.pos[0][0] and self.pos[i][1] == self.pos[0][1] -14:
                    self.pos[i][0] = self.pos[0][0] +14
                    self.pos[i][1] = self.pos[0][1]

                elif self.pos[i][0] == self.pos[0][0] and self.pos[i][1] == self.pos[0][1] +14:
                    self.pos[i][0] = self.pos[0][0] -14
                    self.pos[i][1] = self.pos[0][1]

                elif self.pos[i][0] == self.pos[0][0] - 14 and self.pos[i][1] == self.pos[0][1] - 14:
                    self.pos[i][0] = self.pos[0][0] + 14
                    self.pos[i][1] = self.pos[0][1] -14

                elif self.pos[i][0] == self.pos[0][0] - 14 and self.pos[i][1] == self.pos[0][1] + 14:
                    self.pos[i][0] = self.pos[0][0] -14
                    self.pos[i][1] = self.pos[0][1] -14

                elif self.pos[i][0] == self.pos[0][0] + 14 and self.pos[i][1] == self.pos[0][1] -14:
                    self.pos[i][0] = self.pos[0][0] +14
                    self.pos[i][1] = self.pos[0][1] + 14

                elif self.pos[i][0] == self.pos[0][0] + 14 and self.pos[i][1] == self.pos[0][1] +14:
                    self.pos[i][0] = self.pos[0][0] -14
                    self.pos[i][1] = self.pos[0][1] +14

        if self.pos[0][0] < self.x_left or self.pos[1][0] < self.x_left or self.pos[2][0] < self.x_left or self.pos[3][0] < self.x_left:
            for i in range(0,4):
                self.pos[i][0] += 14

        if self.pos[0][0] > self.x_right + 14*(self.columns-11) or self.pos[1][0] > self.x_right + 14*(self.columns-11) or self.pos[2][0] > self.x_right + 14*(self.columns-11) or self.pos[3][0] > self.x_right + 14*(self.columns-11):
            for i in range(0,4):
                self.pos[i][0] -= 14

        if self.pos[0][1] > self.y_top or self.pos[1][1] > self.y_top or self.pos[2][1] > self.y_top or self.pos[3][1] > self.y_top:
            for i in range(0,4):
                self.pos[i][1] += 14

        if self.pos[0][0] < self.x_left or self.pos[1][0] < self.x_left or self.pos[2][0] < self.x_left or self.pos[3][0] < self.x_left:
            for i in range(0,4):
                self.pos[i][0] += 14

        if self.pos[0][0] > self.x_right + 14*(self.columns-11) or self.pos[1][0] > self.x_right + 14*(self.columns-11) or self.pos[2][0] > self.x_right + 14*(self.columns-11) or self.pos[3][0] > self.x_right + 14*(self.columns-11):
            for i in range(0,4):
                self.pos[i][0] -= 14

        if self.pos[0][1] > self.y_top or self.pos[1][1] > self.y_top or self.pos[2][1] > self.y_top or self.pos[3][1] > self.y_top:
            for i in range(0,4):
                self.pos[i][1] += 14

        self.move_up()

    def move_up(self):
        for i in range(0,4):
            self.pos[i][1] -= 14
