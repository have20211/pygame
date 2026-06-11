import pygame, copy, random
from itertools import groupby
pygame.init()
from settings import *



class Main:
    def __init__(self):
        self.el = [[3,4],[3,3],[3,2]]
        self.apple = [2,5]
        self.wrld = self.generate_map()
        self.direction = (1,0)
        self.a = 0
        self.b = 0
        self.score = 0
        self.run = True
        self.logs = []
        self.font_small = pygame.font.Font(None, 20)
        self.font = pygame.font.Font(None, 64)
        self.text_death = self.font.render('Ты проиграл(', True, (0, 0, 0))
        self.window = pygame.display.get_surface()


    def generate_map(self):
        wrld = []
        a = ['0']*(WIDTH//TILESIZE)
        for i in range(HEIGHT//TILESIZE):
            wrld.append(copy.copy(a))
        return wrld


    def get_direction(self, val):
        if val == 'w' and self.direction != (0,1):
            self.direction = (0,-1)
            self.logs.insert(0, (0,-1))
        if val == 's' and self.direction != (0,-1):
            self.direction = (0,1)
            self.logs.insert(0,  (0,1))
        if val == 'a' and self.direction != (1,0):
            self.direction = (-1,0)
            self.logs.insert(0, (-1,0))
        if val == 'd' and self.direction != (-1,0):
            self.direction =(1,0)
            self.logs.insert(0, (1,0))


    def get_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            return 'w'
        if key[pygame.K_s]:
            return 's'
        if key[pygame.K_a]:
            return 'a'
        if key[pygame.K_d]:
            return 'd'
        if key[pygame.K_r] and not self.run:
            self.el = [[3,4],[3,3],[3,2]]
            self.wrld = self.generate_map()
            self.run = True
        
        try:
            self.logs.pop(100)
        except:
            pass


    def add_events(self):
        coord = [random.randint(0,len(self.wrld)-1),random.randint(0,len(self.wrld[0])-1)]
        if len(self.apple) == 0:
            while coord in self.el:
                coord = [random.randint(0,len(self.wrld)-1), random.randint(0,len(self.wrld[0])-1)]

            self.apple = coord
        self.wrld[self.apple[0]][self.apple[1]] = 'a'


    def check_eat(self, new):
        if new != self.el[1]:
            self.el.insert(0,new)
            if self.el[0] !=  self.apple:
                self.wrld[self.el[len(self.el)-1][0]][self.el[len(self.el)-1][1]] = '0'
                self.el.pop(len(self.el)-1)
            if self.el[0] == self.apple:
                self.apple = []
                self.score += 1
        else:
            new_logs = [el for el, _ in groupby(self.logs)]
            self.direction = new_logs[1]
    

    def check_death(self, new):
        if self.score == WIDTH//TILESIZE*HEIGHT//TILESIZE:
            self.text_death = self.font.render('Ты выиграл(', True, (0, 0, 0))
            self.run = False
        try:
            if self.wrld[new[0]][new[1]] == 'B' and new != self.el[1]:
                return True
            if 0 > new[0] < len(self.wrld)-1 or 0 > new[1] < len(self.wrld[0]):
                return True
        except:
            return True


    def move(self, el):
        self.get_direction(self.get_input())
        if self.a == 10:
            new = [el[0][0]+self.direction[1],el[0][1]+self.direction[0]]
            self.check_eat(new)
            if self.check_death(new):
                self.run = False
                pygame.time.wait(500)
            else:
                for p in range(len(el)):
                    if p == 0:
                        self.wrld[el[p][0]][el[p][1]] = 'H'
                    else:
                        self.wrld[el[p][0]][el[p][1]] = 'B'
            self.a = 0
        else:
            self.a += 1


    def draw(self, wrld):
        for col_index, col in enumerate(wrld):
            for row_index, row in enumerate(col):
                if row == 'a':
                    pygame.draw.rect(self.window, 'red', (row_index*TILESIZE, col_index*TILESIZE, TILESIZE,TILESIZE))
                if row == 'H':
                    pygame.draw.rect(self.window, 'black', (row_index*TILESIZE, col_index*TILESIZE, TILESIZE,TILESIZE))
                if row == 'B':
                    pygame.draw.rect(self.window, 'gray', (row_index*TILESIZE, col_index*TILESIZE, TILESIZE,TILESIZE))


    def execute(self):
        if self.run:
            self.debug = self.font_small.render(f'Счёт: {self.score}', True, (0,0,0))
            self.window.blit(self.debug, (0,0))
            self.add_events()
            self.move(self.el)
            self.draw(self.wrld)
        else:
            self.score = 0
            self.get_input()
            self.window.blit(self.text_death, (WIDTH//4, HEIGHT//2))