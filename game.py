import pygame
from bird import Bird
from pipe import Pipe
import time
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((480, 640))
        self.off_ground_rect = pygame.Rect(0, -600, 480, 1100)
        self.background_image = pygame.image.load("C:/Users/tbcrl/Documents/flappybird/sprites/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1000, 640))
        self.background_speed = 2
        self.pipe = Pipe(self.screen, 6, self.background_speed)
        self.bird = Bird(self.screen, 6, 85)
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
            self.bird.main()
            self.collision_handling()
            pygame.display.update()
            pygame.Clock().tick(60)
        pygame.quit()
    
    def start_screen(self):
        start_screen = True
        while start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
            
            
        self.main()


    def move_background(self):
        if self.background_x <= -999 + self.screen.width:
            self.background_x += 999 - self.screen.width - 19 #the 19 is for offsetting the image to line up when it jumps back
        else:
            self.background_x -= self.background_speed

    def collision_handling(self):
        if not self.bird.bird.colliderect(self.off_ground_rect):
            self.game_over()

        for pipe in self.pipe.top_pipes:
            if self.bird.bird.colliderect(pipe):
                self.game_over()

        for pipe in self.pipe.bottom_pipes:
            if self.bird.bird.colliderect(pipe):
                self.game_over()


    def game_over(self):
        time.sleep(1)
        pygame.quit()