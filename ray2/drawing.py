import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.texture = {'1': pygame.image.load('ray/img/1.png').convert(),
                        '2': pygame.image.load('ray/img/2.png').convert(),
                        '3': pygame.image.load('ray/img/3.png').convert(),
                        'S': pygame.image.load('ray/img/4.png').convert(),
                        }

    def background(self, angle):
        sky_offset = -5 * math.degrees(angle) % WIDTH
        self.sc.blit(self.texture['S'], (sky_offset, 0))
        self.sc.blit(self.texture['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.texture['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.texture)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle), 
                                                map_y + 12 * math.sin(player.angle)))
        pygame.draw.circle(self.sc_map, RED,(int(map_x), int(map_y)), 5)
        for x,y in mini_map:
            pygame.draw.rect(self.sc_map, GREEN, (x,y,MAP_TILE,MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)