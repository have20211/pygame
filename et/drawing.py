import pygame
from settings import *
from player import Input

pygame.init()







class DrawShop():
    def __init__(self, shop):
        self.shop = shop
        self.input = Input()
        self.screen = pygame.display.get_surface()
        self.font_count = pygame.font.SysFont('Arial', 16, bold=True)
        self.font = pygame.font.SysFont('Arial', 20, bold=True)
        self.color = (40, 40, 40)

    def draw(self):
        for item in range(len(self.shop.items)):
            col = (item // 5) * 4
            row = item % 5
            if pygame.Rect(col*TILE,row*(TILE+SHOP_COUNT_OFFSET),TILE*4,TILE).colliderect(pygame.Rect(self.input.get_pos_mouse()[0],self.input.get_pos_mouse()[1],1,1)):
                if self.input.get_click_mouse(1):
                    self.shop.index = item


            self.draw_rect(item, col, row)
    
    def draw_rect(self, index, x, y):
        #иконка и количество
        count = self.font_count.render(str(self.shop.items[index]['count']), 0, WHITE)
        count_rect = count.get_rect(bottomright=(x*TILE+TILE - SHOP_COUNT_OFFSET, y*(TILE+SHOP_COUNT_OFFSET)+TILE))

        self.screen.blit(self.shop.items[index]['icon'], (x*TILE,y*(TILE+SHOP_COUNT_OFFSET)))
        self.screen.blit(count, count_rect)

        #информация 
        name = self.font.render(str(self.shop.items[index]['name']), 0, WHITE)
        name_rect = name.get_rect(bottomleft=(x*TILE+TILE+SHOP_COUNT_OFFSET, y*(TILE+SHOP_COUNT_OFFSET)-SHOP_COUNT_OFFSET+TILE))
        price = self.font.render(str(self.shop.items[index]['price']), 0, YELLOW)
        price_rect = price.get_rect(bottomleft=(x*TILE+TILE*3+SHOP_COUNT_OFFSET, y*(TILE+SHOP_COUNT_OFFSET)-SHOP_COUNT_OFFSET+TILE))
        if index == self.shop.index:
            pygame.draw.rect(self.screen, DARKGRAY, (x*TILE+TILE, y*(TILE+SHOP_COUNT_OFFSET), TILE*3, TILE))
        else:
            pygame.draw.rect(self.screen, GRAY, (x*TILE+TILE, y*(TILE+SHOP_COUNT_OFFSET), TILE*3, TILE))
        self.screen.blit(name, name_rect)
        self.screen.blit(price, price_rect)

