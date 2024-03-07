import pygame
import color
import numpy as np
dx = [0, 0, -20, 20, 0]
dy = [-20, 20, 0, 0, 0]

class Snake():
    def __init__(self, colorHead = color.RED, colorBody = color.WHITE):
        self.length = 3
        self.moved = 0
        self.colorHead = colorHead
        self.colorBody = colorBody
        self.list = np.array([[290, 230], [310, 230], [330, 230]])
        self.dir = 1
    def changeDir(self, dir):
        if self.dir == 0:
            if dir != 1:
                self.dir = dir
                self.moved = 0
        if self.dir == 1:
            if dir != 0:
                self.dir = dir
                self.moved = 0
        if self.dir == 2:
            if dir != 3:
                self.dir = dir
                self.moved = 0
        if self.dir == 3:
            if dir != 2:
                self.dir = dir
                self.moved = 0
    def draw(self, screen):
        for i, pos in enumerate(self.list):
            if i == 0:
                pygame.draw.circle(screen, self.colorHead, pos, 10)
            else:
                pygame.draw.circle(screen, self.colorBody, pos, 10)
    def move(self):
        if self.moved == 1:
            return
        self.moved = 1
        for i in range(self.length-1, 0, -1):
            if (i > 0):
                self.list[i] = self.list[i-1]
        self.list[0][0] += dx[self.dir]
        self.list[0][1] += dy[self.dir]
    def gameOver(self):
        if self.list[0][0] <= 60 or self.list[0][1] <= 60 or self.list[0][0] >= 540 or self.list[0][1] >= 540:
            return True
        for i in range(len(self.list)):
            if i > 0 and self.list[0][0] == self.list[i][0] and self.list[0][1] == self.list[i][1]:
                return True
        return False