import pygame,sys,time
from settings import *
from level import Main
pygame.init()




class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.main = Main()
        
    def run(self):
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
            self.window.fill('white')
            self.main.execute()
            pygame.display.update()
            self.clock.tick(60)
                


if __name__ == "__main__":
    game = Game()
    game.run()