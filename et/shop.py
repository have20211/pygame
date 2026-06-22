import pygame
from settings import *
from drawing import DrawShop
pygame.init()






class Shop:
    def __init__(self):
        self.items = [
            {'name': 'сумка', 'count': 2, 'price': 100, 'icon': pygame.transform.scale( pygame.image.load('et/image/sumk.png').convert(), (TILE, TILE))},
            {'name': 'мана', 'count': 4, 'price': 200, 'icon': pygame.transform.scale( pygame.image.load('et/image/sumk.png').convert(), (TILE, TILE))},
            {'name': 'херня', 'count': 2, 'price': 100, 'icon': pygame.transform.scale( pygame.image.load('et/image/sumk.png').convert(), (TILE, TILE))},
            {'name': 'сумка', 'count': 2, 'price': 100, 'icon': pygame.transform.scale( pygame.image.load('et/image/sumk.png').convert(), (TILE, TILE))},
            {'name': 'мана', 'count': 4, 'price': 200, 'icon': pygame.transform.scale( pygame.image.load('et/image/sumk.png').convert(), (TILE, TILE))},
            {'name': 'херня', 'count': 2, 'price': 100, 'icon': pygame.transform.scale( pygame.image.load('et/image/sumk.png').convert(), (TILE, TILE))},
            {'name': 'сумка', 'count': 2, 'price': 100, 'icon': pygame.transform.scale( pygame.image.load('et/image/sumk.png').convert(), (TILE, TILE))},
            {'name': 'мана', 'count': 4, 'price': 200, 'icon': pygame.transform.scale( pygame.image.load('et/image/sumk.png').convert(), (TILE, TILE))},
            {'name': 'херня', 'count': 2, 'price': 100, 'icon': pygame.transform.scale( pygame.image.load('et/image/sumk.png').convert(), (TILE, TILE))},

        ]
        self.index = 0




