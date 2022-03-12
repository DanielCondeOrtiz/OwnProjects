import numpy as np
from random import randint
import copy

class Grid:
    def __init__(self):
        self.current = np.zeros((30,20))
        start = [randint(0,29),randint(0,19)]
        self.current[start[0]][start[1]] = 600
        self.length = 1
        self.moving = 0
        self.apple = None
        self.gen_apple()
        self.eaten = False

    def gen_apple(self):
        self.apple = [randint(0,29),randint(0,19)]

        while self.current[self.apple[0]][self.apple[1]] != 0:
            self.apple = [randint(0,29),randint(0,19)]

    def move(self,move,count):
        if count % 4 == 0:
            if move == 0:
                move = self.moving
            elif move == 1 and self.moving == 2:
                move = 2
            elif move == 2 and self.moving == 1:
                move = 1
            elif move == 3 and self.moving == 4:
                move = 4
            elif move == 4 and self.moving == 3:
                move = 3

            positions = []
            sum = 0
            if self.eaten:
                sum = -1
            for i in range(0,self.length):
                pos = np.nonzero(self.current==(600 -i))
                positions.append([pos[0][0],pos[1][0]])

            if move == 1:
                #up
                self.moving = move
                i=1
                if positions[0][1] != 0:
                    if self.current[positions[0][0]][positions[0][1] - 1] == 0:
                        self.current[positions[0][0]][positions[0][1] - 1] = 600
                        for item in positions:
                            self.current[item[0]][item[1]] = 600 -i
                            i+=1

                        if self.eaten:
                            self.eaten = False
                            self.length +=1
                            self.current[positions[-1][0]][positions[-1][1]] = 601-i
                        else:
                            self.current[positions[-1][0]][positions[-1][1]] = 0
                    else:
                        return True
                else:
                    return True

            elif move == 2:
                #down
                self.moving = move
                i=1
                if positions[0][1] != 19:
                    if self.current[positions[0][0]][positions[0][1] + 1] == 0:
                        self.current[positions[0][0]][positions[0][1] + 1] = 600
                        for item in positions:
                            self.current[item[0]][item[1]] = 600 -i
                            i+=1

                        if self.eaten:
                            self.eaten = False
                            self.length +=1
                            self.current[positions[-1][0]][positions[-1][1]] = 601-i
                        else:
                            self.current[positions[-1][0]][positions[-1][1]] = 0
                    else:
                        return True
                else:
                    return True

            elif move == 3:
                #left
                self.moving = move
                i=1
                if positions[0][0] != 0:
                    if self.current[positions[0][0] -1][positions[0][1]] == 0:
                        self.current[positions[0][0] -1][positions[0][1]] = 600
                        for item in positions:
                            self.current[item[0]][item[1]] = 600 -i
                            i+=1

                        if self.eaten:
                            self.length +=1
                            self.eaten = False
                            self.current[positions[-1][0]][positions[-1][1]] = 601-i
                        else:
                            self.current[positions[-1][0]][positions[-1][1]] = 0
                    else:
                        return True
                else:
                    return True

            elif move == 4:
                #right
                self.moving = move
                i=1
                if positions[0][0] != 29:
                    if self.current[positions[0][0] +1][positions[0][1]] == 0:
                        self.current[positions[0][0]+1][positions[0][1]] = 600
                        for item in positions:
                            self.current[item[0]][item[1]] = 600 -i
                            i+=1

                        if self.eaten:
                            self.eaten = False
                            self.length +=1
                            self.current[positions[-1][0]][positions[-1][1]] = 601-i
                        else:
                            self.current[positions[-1][0]][positions[-1][1]] = 0
                    else:
                        return True
                else:
                    return True

            if positions[0][0] == self.apple[0] and positions[0][1] == self.apple[1]:
                self.gen_apple()
                self.eaten = True

        if count % 20 == 0:
            self.eaten = True


        return False

    def clear(self):
        self.current = np.zeros((30,20))
