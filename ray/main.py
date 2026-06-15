import pygame, math
from settings import *
from map import world_map
from player import Player
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()


sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)


while True:
    [exit() for event in pygame.event.get() if event.type == pygame.QUIT]


    player.movement()
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)



    pygame.display.update()
    clock.tick(FPS)