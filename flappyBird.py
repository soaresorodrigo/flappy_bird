import os, sys, pygame, random, math
from pygame.locals import *
from pagFunctions import *
from pagClasses import *

pygame.init()
screen = pygame.display.set_mode((300, 500))
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT + 1 , 2000)
pygame.display.set_icon(pygame.image.load('images/iconBird.png'))
pygame.display.set_caption(" | Flappy Bird |")

gameImages = load_images()
gameFloor = Floor(gameImages['ground'])
gameBird = Bird()
gamePipes = []



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == USEREVENT + 1:
            pipes = Pipe(300, False)
            gamePipes.append(pipes)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gameBird.steps_to_jump = 15
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                gameBird.steps_to_jump = 15

    screen.blit(gameImages['background'], (0, 0))
    screen.blit(gameImages['ground'], (0, 500 - 73))
    #Add tubes with a gap between them
    for pipes in gamePipes:
        pipes.x -= 2
        if pipes.x <= - pipeW:
            gamePipes.remove(pipes)
        else:
            screen.blit(gameImages['upPipe'], (pipes.x, pipes.topH))
            screen.blit(gameImages['downPipe'], (pipes.x, pipes.bottomH))

    gameBird.update_position()
    gameBird.draw_bird(screen, gameImages['upFlap'], gameImages['downFlap'])
    gameFloor.draw_floor(screen)


    pygame.display.update()
    clock.tick(60)


