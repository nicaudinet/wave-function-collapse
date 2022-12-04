import pygame
import numpy as np
import sys
import copy
import random

from lib.tile import Tile
from lib.grid import Grid

FPS = 20

TILE_SIZE = 50
DIM = 10
WINDOW_HEIGHT = DIM * TILE_SIZE
WINDOW_WIDTH = DIM * TILE_SIZE

images = {
    'blank': pygame.image.load("tiles/demo/blank.png"),
    'up': pygame.image.load("tiles/demo/up.png"),
    'right': pygame.image.load("tiles/demo/right.png"),
    'down': pygame.image.load("tiles/demo/down.png"),
    'left': pygame.image.load("tiles/demo/left.png")
    }

tiles = [
    Tile(images['blank'], [0,0,0,0]),
    Tile(images['up'], [1,1,0,1]),
    Tile(images['right'], [1,1,1,0]),
    Tile(images['down'], [0,1,1,1]),
    Tile(images['left'], [1,0,1,1])
    ]

for tile in tiles:
    tile.analyze(tiles)
    
grid = Grid(DIM, tiles)

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
        grid.draw(canvas)
        grid.update()

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
