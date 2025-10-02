import pygame
import sys
import time

import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
board = ttt.initial_state()
ai_turn = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
import pygame
import sys
import time

import tictactoe as ttt

pygame.init()
size = width, height = 600, 400

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
board = ttt.initial_state()
ai_turn = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    if user is None:
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

