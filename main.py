import pygame
import numpy as np
import sys

FPS = 11

CELL_SIZE = 10
HEIGHT = 100
WIDTH = 100
WINDOW_HEIGHT = HEIGHT * CELL_SIZE
WINDOW_WIDTH = WIDTH * CELL_SIZE

pygame.init()
clock = pygame.time.Clock()
canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wave Function Collapse")

animate = True
exit = False

export = False
counter = 0
if len(sys.argv) == 3:
    if sys.argv[1] == "--export": 
        export = True
        frame_name = sys.argv[2] + "/frame_{0:05d}.png"

while not exit:

    if export:
        pygame.image.save(canvas, frame_name.format(counter))
        counter += 1

    clock.tick(FPS)

    if animate:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.unicode == 'q':
                exit = True
            if event.unicode == ' ':
                animate = not animate
            if event.key == 1073741906: # Up arrow
                FPS = min(61, FPS + 5)
            if event.key == 1073741905: # Down arrow
                FPS = max(1, FPS - 5)

    pygame.display.update()
