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
        self.pipe = Pipe(self.screen, 4, self.background_speed)
        self.bird = Bird(self.screen, 6, 85)
        self.background_x = 0
        self.game_running = True
        


    
    def main(self):
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

            self.move_background()
            self.pipe.main()
            self.display_score()
            self.bird.main()
            self.collision_handling()
            pygame.display.update()
            pygame.Clock().tick(60)
        pygame.quit()
    
    def start_screen(self):
        start_screen_image = pygame.image.load("C:/Users/tbcrl/Documents/flappybird/sprites/gamestart.png")
        start_screen_image = pygame.transform.scale(start_screen_image, (self.screen.width-80, self.screen.height-80))
        start_screen = True
        while start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_screen = False
                    pygame.quit()

            self.move_background()
            self.screen.blit(start_screen_image, (40, 40))
            self.bird.animate()
            pygame.display.update()
            pygame.Clock().tick(60)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                start_screen = False
                self.bird.angle = 32
            
                    
            
            
        self.main()


    def move_background(self):
        self.screen.blit(self.background_image, (self.background_x, 0))

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
        self.reset()


    def reset(self):
        self.bird.bird.y = 400
        self.bird.angle = 0
        self.pipe.top_pipes.clear()
        self.pipe.bottom_pipes.clear()
        self.start_screen()

    def display_score(self):
        score = self.pipe.get_score()
        print(score)
        