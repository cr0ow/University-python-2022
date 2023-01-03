import sys
import pygame
from random import random

FPS = 60
counter = 0
loose = False
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

width = 500
height = 600

snowflakes = []
flake_size = 40


def add_snowflake():
    left = max(0, int(random() * width - flake_size))
    return pygame.Rect(left, 0, flake_size, flake_size)


def check_hit(pos):
    for flake in snowflakes:
        if flake.left < pos[0] < flake.right and flake.top < pos[1] < flake.bottom:
            return flake
    return None


pygame.init()
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SnowFlakes')

while not loose:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hit = check_hit(event.pos)
            if isinstance(hit, pygame.Rect):
                snowflakes.remove(hit)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    counter += 1
    if counter == FPS:
        snowflakes.append(add_snowflake())
        counter = 0

    screen.fill(black)
    for snowflake in snowflakes:
        pygame.draw.rect(screen, white, snowflake)
        snowflake.y += 1
        if snowflake.bottom == height:
            loose = True

    pygame.display.flip()
    clock.tick(FPS)


