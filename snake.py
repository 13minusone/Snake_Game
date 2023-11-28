import pygame
import color
import setting
import numpy as np

dx = [0, 0, -20, 20]
dy = [-20, 20, 0, 0]

class Snake():
    def __init__(self, colorHead = color.RED, colorBody = color.WHITE):
        self.length = 6
        self.colorHead = colorHead
        self.colorBody = colorBody
        self.list = np.array([[270, 250], [290, 250], [310, 250], [330, 250], [350, 250], [-1,-1]])
        self.dir = 1
    def draw(self, screen):
        for i in range(0,self.length - 2,1):
            pos = self.list[i]
            if i == 0:
                pygame.draw.circle(screen, self.colorHead, pos, 10)
            else:
                pygame.draw.circle(screen, self.colorBody, pos, 10)
    def move(self):
        self.list[self.length - 1] = self.list[self.length - 2]
        for i in range(self.length-2, 0, -1):
            if (i > 0):
                self.list[i] = self.list[i-1]
        self.list[0][0] += dx[self.dir]
        self.list[0][1] += dy[self.dir]
    def create(self):
        self.length += 1
        self.list = np.append(self.list, [[-1,-1]], axis = 0)
class Food():
    def __init__(self, Color = color.RED):
        self.list = np.array([[70,70]])
        for i in range(60, setting.screen_height - 60 + 1, 20):
            for j in range(60, setting.screen_width - 60 + 1, 20):
                self.list = np.append(self.list, [[i + 10, j + 10]], axis = 0)
        self.Color = Color
        