import pygame
from settings import *
pygame.init()





class Inventory():
    def __init__(self):
        self.items = [
            {'name': 'Золото', 'count': 1000},
            {'name': 'Меч', 'count': 1},
        ]



class Input():
    def __init__(self):
        pass

    def get_pos_mouse(self):
        return pygame.mouse.get_pos()

    def get_click_mouse(self, key):
        if pygame.mouse.get_pressed()[key]:
            return True
        else:
            return False