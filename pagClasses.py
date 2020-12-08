import math, pygame
from random import randint
birdH = 24
birdW = 34
pipeH = 320
pipeW = 52

class Floor:
    #game floor positioning
    def __init__(self, image):
        self.x = 0
        self.y = 500 - 73
        self.image = image
    # drawing and moving from the floor
    def draw_floor(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.x -= 3
        if(self.x < - 300):
            self.x = 0

class Bird:
    def __init__(self):
        self.bird_x = 300 / 2 - (birdW / 2)
        self.bird_y = 500 / 2 - (birdH / 2)
        self.steps_to_jump = 0
    def update_position(self):
        if self.steps_to_jump > 0:
            self.bird_y -= (1 - math.cos((15 - self.steps_to_jump) * math.pi)) * 4
            self.steps_to_jump -= 1
        else:
            self.bird_y += 3
    def draw_bird(self, screen, image_1, image_2):
        if pygame.time.get_ticks() % 100 >= 350 :
            screen.blit(image_1, (self.bird_x, self.bird_y))
        else:
            screen.blit(image_2, (self.bird_x, self.bird_y))

class Pipe:
    def __init__(self, x, score_counted):
        self.x = 300
        self.topH = randint(50, 250) - pipeH
        self.bottomH = self.topH + pipeH + (4 * birdH)
        self.score_counted = score_counted

