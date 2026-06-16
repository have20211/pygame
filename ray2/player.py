from settings import *
import pygame, math
pygame.init()



class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle


    @property
    def pos(self):
        return(self.x, self.y)


    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y += player_speed * math.sin(self.angle)
            self.x += player_speed * math.cos(self.angle)
        if keys[pygame.K_s]:
            self.y -= player_speed * math.sin(self.angle)
            self.x -= player_speed * math.cos(self.angle)
        if keys[pygame.K_a]:
            self.y -= player_speed * math.cos(self.angle)
            self.x += player_speed * math.sin(self.angle)
        if keys[pygame.K_d]:
            self.y += player_speed * math.cos(self.angle)
            self.x -= player_speed * math.sin(self.angle)
        if keys[pygame.K_LEFT]:
            self.angle -= 0.04
        if keys[pygame.K_RIGHT]:
            self.angle += 0.04
