import pygame
from bird import Bird
from pipe import Pipe
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((480, 640))
        self.background_image = pygame.image.load("C:/Users/tbcrl/Documents/flappybird/sprites/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1000, 640))
        self.background_speed = 1
        self.pipe = Pipe(self.screen, 6, self.background_speed)
        self.background_x = 0
        self.game_running = True
        


    
    def main(self):
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

            self.screen.blit(self.background_image, (self.background_x, 0))
            self.move_background()
            self.pipe.main()
            pygame.display.update()
            pygame.Clock().tick(60)
        pygame.quit()
    
    def main_menu(self):
        self.main()


    def move_background(self):
        if self.background_x <= -999 + self.screen.width:
            self.background_x += 999 - self.screen.width - 19 #the 19 is for offsetting the image to line up when it jumps back
        else:
            self.background_x -= self.background_speed