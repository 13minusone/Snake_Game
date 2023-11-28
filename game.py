import pygame, numpy as np, setting
import random
from snake import Snake
from snake import Food
from color import BLACK, RED, WHITE
#######################
#Display
wScreen, hScreen = 800, 600
screen = pygame.display.set_mode((wScreen, hScreen))
clock = pygame.time.Clock()
#######################
'''class Snake():
    def __init__(self):
        self.dx = [0, 0, -1, 1]
        self.dy = [-1, 1, 0, 0]
        self.dir = random.randint(0, 3)
        self.length = 1
        self.list = [[wScreen/2, hScreen/2]]
    def changeDir(self, dir):
        if self.dir == 0 or self.dir == 1:
            if dir != 0 and dir != 1:
                self.dir = dir
        if self.dir == 2 or self.dir == 3:
            if dir != 2 and dir != 3:
                self.dir = dir
    def render(self, surface, color = WHITE, size = 20):
        self.rect = []
        for x,y in self.list:
            self.rect.append(pygame.draw.rect(surface, color, (x, y, size, size)))
    def move(self):
        x = self.list[0][0] + self.dx[self.dir]
        y = self.list[0][1] + self.dy[self.dir]
        if x <= -5 or x >= wScreen - 5 or y <= -5 or y >= hScreen - 5:
            return
        prex, prey = 0, 0
        for i, arr in enumerate(self.list):
            if i > 0:
                self.list[i] = [prex, prey]
            prex, prey = arr[0], arr[1]
        self.list[0] = [x, y]
    def collision(self, food):
        if self.rect[0].colliderect(food):
            return True
        return False
class Food():
    def __init__(self):
        self.x = random.randint(10, wScreen-10)
        self.y = random.randint(10, hScreen-10)
        self.color = RED
    def move(self):
        self.x = random.randint(10, wScreen-10)
        self.y = random.randint(10, hScreen-10)
    def render(self, surface, color = RED):
        self.circle = pygame.draw.circle(surface, color, (self.x, self.y), 10)
    

snake = Snake()
food = Food()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.changeDir(0)
            if event.key == pygame.K_DOWN:
                snake.changeDir(1)
            if event.key == pygame.K_LEFT:
                snake.changeDir(2)
            if event.key == pygame.K_RIGHT:
                snake.changeDir(3)
    food.render(screen)
    snake.render(screen, BLACK)
    snake.move()
    if snake.collision(food.circle):
        food.render(screen, BLACK)
        food.move()
        lastx, lasty = snake.list[len(snake.list) - 1][0], snake.list[len(snake.list) - 1][1]
        snake.list.append([lastx, lasty])
        snake.move()
        #print(snake.list)
    snake.render(screen)
    pygame.display.update()
    clock.tick(120)
    '''
# arr = np.array([[1, 2], [2, 3]])
# arr = np.append(arr, [[0, 0]], axis = 0)
# print(arr)
def displayBoard(screen, boardColor = WHITE):
    for i in range(60, setting.screen_height - 60 + 1, 20):
        x1, y1 = 60, i
        x2, y2 = setting.screen_width - 60, i
        pygame.draw.line(screen, boardColor, (x1, y1), (x2, y2), 1)
    for i in range(60, setting.screen_width - 60 + 1, 20):
        x1, y1 = i, 60
        x2, y2 = i, setting.screen_height - 60
        pygame.draw.line(screen, boardColor, (x1, y1), (x2, y2), 1)
snake = Snake()
food = Food()
def DrawFood():
    n = len(food.list)
    m = len(snake.list) 
    global foodx
    global foody
    while True:
        i = random.randint(0,n - 1)
        k = 0
        for j in range(m - 2, 0, -1):
            if food.list[i][0] == snake.list[j][0] and food.list[i][1] == snake.list[j][1]:
                k = 1
                break
        if k == 0:
            foodx = food.list[i][0]
            foody = food.list[i][1]
            break

running = True
DrawFood()
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.dir = 0
            if event.key == pygame.K_DOWN:
                snake.dir = 1
            if event.key == pygame.K_LEFT:
                snake.dir = 2
            if event.key == pygame.K_RIGHT:
                snake.dir = 3
    displayBoard(screen)
    pygame.draw.circle(screen, food.Color, (foodx, foody), 10)
    print(foodx)
    print(foody)
    if foodx == snake.list[0][0] and foody == snake.list[0][1]:
        DrawFood()
        snake.create()
    snake.move()
    snake.draw(screen)
    pygame.display.update()
    clock.tick(5)