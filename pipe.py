import pygame
import random
class Pipe:
    def __init__(self, screen, frequency, speed):
        self.frequency = (10 - frequency)*60
        self.screen = screen
        self.pipe_image = pygame.image.load("C:/Users/tbcrl/Documents/flappybird/sprites/pipe.png") 
        self.pipe_image = pygame.transform.scale(self.pipe_image, (50, 300))
        self.clip_rect = pygame.Rect(0, -600, 480, 1127)
        self.top_pipes = []
        self.bottom_pipes = []
        self.timer = 100
        self.speed = speed

    def main(self):
        if self.timer >= self.frequency:
            self.timer = 0
            self.add_pipe()
        else:
            self.timer += 1

        self.handle_movement()
            

    def blit_pipe(self, x, y, flipped = False):
        self.screen.set_clip(self.clip_rect)

        if flipped:
            new_image = pygame.transform.rotate(self.pipe_image, 180)
            self.screen.blit(new_image, (x, y)) 
        else:
            self.screen.blit(self.pipe_image, (x, y))

        self.screen.set_clip(None)


    def add_pipe(self):
        y = random.randint(225, 400)
        self.bottom_pipes.append(pygame.Rect(520, y, 50, 300))
        self.top_pipes.append(pygame.Rect(520, y-425, 50, 300))
    
    def handle_movement(self):
        for pipe in self.bottom_pipes:
            if pipe.x < -80:
                self.bottom_pipes.remove(pipe)
            else:
                pipe.x -= self.speed
                self.blit_pipe(pipe.x, pipe.y)
        
        for pipe in self.top_pipes:
            if pipe.x < -80:
                self.top_pipes.remove(pipe)
            else:
                pipe.x -= self.speed
                self.blit_pipe(pipe.x, pipe.y, True)

        