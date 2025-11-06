import pygame
class Bird:
    def __init__(self, screen, flap_height, flap_speed):
        self.flap_height = flap_height
        self.flap_speed = 100 - flap_speed
        self.flap_state = True
        self.flap_triggered = False
        self.timer = 0
        self.screen = screen
        self.gravity = 0.4 # gravity controls the rate at which the bird transitions into a freefall and max gravity controls the max speed that the bird can fall at
        self.max_gravity = 7
        self.angle = 0
        self.angle_vel = 0
        self.angle_gravity = 0.17# angle gravity controls are the same as the regular gravity controls.
        self.max_angle_gravity = 7
        self.y_vel = 0
        self.bird_wingsup = pygame.image.load("C:/Users/tbcrl/Documents/flappybird/sprites/bird_wingsup.png")
        self.bird_wingsup = pygame.transform.scale(self.bird_wingsup, (45, 32))
        self.bird_wingsdown = pygame.image.load("C:/Users/tbcrl/Documents/flappybird/sprites/bird_wingsdown.png")
        self.bird_wingsdown = pygame.transform.scale(self.bird_wingsdown, (45, 32))
        self.bird = pygame.Rect(80, 300, 45, 32)


    def main(self):
        self.animate()
        self.flap()
    def animate(self):
        if self.timer >= self.flap_speed:
            self.timer = 0
            if self.flap_state:
                self.flap_state = False
            else:
                self.flap_state = True
        else:
            self.timer += 1

        if self.flap_state:
            self.rotated_image = pygame.transform.rotate(self.bird_wingsup, self.angle)
        else:
            self.rotated_image = pygame.transform.rotate(self.bird_wingsdown, self.angle)
            
        self.screen.blit(self.rotated_image, self.bird)

    def flap(self):
        if self.y_vel < self.max_gravity:
            self.y_vel -= self.gravity
        
        self.bird.y -= self.y_vel
        if self.angle_vel < self.max_angle_gravity:
            self.angle_vel += self.angle_gravity
        if not self.angle <= -90:
            self.angle -= self.angle_vel

        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            if not self.flap_triggered:
                self.y_vel = self.flap_height
                self.angle = 34
                self.angle_vel = 0
                self.flap_triggered = True
        else:
            self.flap_triggered = False



        
        
            
        
