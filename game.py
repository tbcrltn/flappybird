import pygame
from bird import Bird
from pipe import Pipe
import time
class Game:
    def __init__(self):
        pygame.init()
        self.click = False
        self.screen = pygame.display.set_mode((480, 640))
        self.off_ground_rect = pygame.Rect(0, -600, 480, 1100)
        self.background_image = pygame.image.load("sprites/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (1000, 640))
        self.background_speed = 2
        self.pipe = Pipe(self.screen, 4, self.background_speed)
        self.bird = Bird(self.screen, 6, 85)
        self.background_x = 0
        self.game_running = True
        self.die_sound = pygame.mixer.Sound("sounds/die.mp3")
        self.hit_sound = pygame.mixer.Sound("sounds/hit.mp3")
        self.swoosh_sound = pygame.mixer.Sound("sounds/swoosh.mp3")
        self.in_game = True
        


    
    def main(self):
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click = True
                else:
                    self.click = False


            self.screen.blit(self.background_image, (self.background_x, 0))
            if self.in_game:
                self.move_background()
                self.pipe.main()
                self.display_score()
                self.bird.main()
                self.collision_handling()   
            elif not self.in_game:
                self.game_over_screen()
            pygame.display.update()
            pygame.Clock().tick(60)
        pygame.quit()
    
    def start_screen(self):
        start_screen_image = pygame.image.load("sprites/gamestart.png")
        start_screen_image = pygame.transform.scale(start_screen_image, (self.screen.width-80, self.screen.height-80))
        start_screen = True
        while start_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_screen = False
                    pygame.quit()
            self.screen.blit(self.background_image, (self.background_x, 0))
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
        self.in_game = False
        self.hit_sound.play()
        time.sleep(0.7)
        self.die_sound.play()
        time.sleep(1)
        if self.pipe.get_score() > self.read_high_score():
            self.write_high_score(self.pipe.get_score())

    
    def game_over_screen(self):
        pixel_font = pygame.font.Font("fonts/pixel.ttf", 30)
        high_score = self.read_high_score()
        background = pygame.Surface((300, 150))

        game_over_image = pygame.image.load("sprites/gameover.png")
        game_over_image = pygame.transform.scale(game_over_image, (380, 75))

        background.fill((252, 226, 154))

        pygame.draw.rect(background, (0,0,0), background.get_rect(), width = 3)
        self.screen.blit(game_over_image, (self.screen.width/2 - game_over_image.width/2, 150))

        score_text = pixel_font.render(f"SCORE:  {self.pipe.get_score()}", False, (0, 0, 0))
        highscore_text = pixel_font.render(f"HIGH SCORE:  {high_score}", False, (0, 0, 0))

        background.blit(score_text, (background.get_width()/2 - score_text.get_width()/2, 40))
        background.blit(highscore_text, (background.get_width()/2 - highscore_text.get_width()/2, 90))
        self.screen.blit(background, (self.screen.width/2 - background.get_width() /2, self.screen.height/2 - background.get_height()/2))

        self.make_buttons(pixel_font)


        

    def make_buttons(self, pixel_font):
        mouse = pygame.mouse.get_pos()
        play_button = pygame.draw.rect(self.screen, (252, 226, 154), (self.screen.width/2 - 140, 400,280, 50), border_radius = 7)
        play_button_text = pixel_font.render("PLAY AGAIN", False, (255, 197, 38))
        if play_button.collidepoint(mouse):
            play_button = pygame.draw.rect(self.screen, (255, 197, 38), (self.screen.width/2 - 140, 400,280, 50), border_radius = 7)
            play_button_text = pixel_font.render("PLAY AGAIN", False, (252, 226, 154))
            if self.click:
                self.reset()
        self.screen.blit(play_button_text, (play_button.x+50, play_button.y+10))

        leave_button = pygame.draw.rect(self.screen, (252, 226, 154), (self.screen.width/2 - 140, 465,280, 50), border_radius = 7)
        leave_button_text = pixel_font.render("EXIT", False, (255, 197, 38))
        if leave_button.collidepoint(mouse):
            leave_button = pygame.draw.rect(self.screen, (255, 197, 38), (self.screen.width/2 - 140, 465,280, 50), border_radius = 7)
            leave_button_text = pixel_font.render("EXIT", False, (252, 226, 154))
            if self.click:
                pygame.quit()
        self.screen.blit(leave_button_text, (leave_button.x+105, leave_button.y+10))


    def read_high_score(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0
        
    def write_high_score(self, score):
        with open("highscore.txt", "w") as f:
            f.write(str(score))



        
        


    def reset(self):
        self.swoosh_sound.play()
        self.in_game = True
        self.bird.bird.y = 400
        self.bird.angle = 0
        self.pipe.score = 0
        self.pipe.frequency = self.pipe.start_frequency
        self.pipe.top_pipes.clear()
        self.pipe.bottom_pipes.clear()
        self.start_screen()



    def display_score(self):
        score = self.pipe.get_score()
        split_score = list(str(score))
        if len(split_score) == 1:
            split_score.insert(0, None)
            split_score.insert(0, None)
        elif len(split_score) == 2:
            split_score.insert(0, None)

        if split_score[0] != None:
            score_000_image = pygame.image.load(f"sprites/{split_score[0]}.png")
            score_00_image = pygame.image.load(f"sprites/{split_score[1]}.png")
            score_0_image = pygame.image.load(f"sprites/{split_score[2]}.png")
            self.screen.blit(score_000_image, (self.screen.width/2 - score_000_image.width/2 - 24, 100))
            self.screen.blit(score_00_image, (self.screen.width/2 - score_00_image.width/2, 100))
            self.screen.blit(score_0_image, (self.screen.width/2 - score_0_image.width/2 + 24, 100))
        elif split_score[1] != None:
            score_00_image = pygame.image.load(f"sprites/{split_score[1]}.png")
            score_0_image = pygame.image.load(f"sprites/{split_score[2]}.png")
            self.screen.blit(score_00_image, (self.screen.width/2 - score_00_image.width/2 - 12, 100))
            self.screen.blit(score_0_image, (self.screen.width/2 - score_0_image.width/2 + 12, 100))
        else:
            score_0_image = pygame.image.load(f"sprites/{split_score[2]}.png")
            self.screen.blit(score_0_image, (self.screen.width/2 - score_0_image.width/2, 100))
        