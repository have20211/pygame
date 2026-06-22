import pygame
from settings import *
from shop import Shop
from drawing import DrawShop
pygame.init()





class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.shop = Shop()
        self.drawshop = DrawShop(self.shop)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            self.screen.fill(BLACK)
            self.drawshop.draw()
            pygame.display.update()
            self.clock.tick(FPS)



if __name__ == "__main__":
    game = Game()
    game.run()