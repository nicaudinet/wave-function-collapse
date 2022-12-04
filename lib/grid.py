from lib.cell import Cell
from itertools import repeat
import copy
import random
from functools import reduce

def reduce_union(sets):
    return reduce(lambda a, b: a | b, sets)

class Grid:
    def __init__(self, dim, tiles):
        self.dim = dim
        self.tiles = tiles
        self.cells = [Cell() for i in range(dim * dim)]
        self.full = False

    def update_cell(self, i, j):
        index = i * self.dim + j
        cell = self.cells[index]
        if not cell.collapsed:
            options = set(range(5))
            # Look up
            if j > 0:
                up = self.cells[i * self.dim + j - 1]
                possible = [self.tiles[option].down for option in up.options]
                options &= reduce_union(possible)
            # Look right
            if i < self.dim - 1:
                right = self.cells[(i + 1) * self.dim + j]
                possible = [self.tiles[option].left for option in right.options]
                options &= reduce_union(possible)
            # Look down
            if j < self.dim - 1:
                down = self.cells[i * self.dim + j + 1]
                possible = [self.tiles[option].up for option in down.options]
                options &= reduce_union(possible)
            # Look left
            if i > 0:
                left = self.cells[(i - 1) * self.dim + j]
                possible = [self.tiles[option].right for option in left.options]
                options &= reduce_union(possible)
            cell.options = options

    def update(self):
        if not self.full:
            # Find cell with lowest entropy
            cells = copy.copy(self.cells)
            cells.sort(key=lambda cell: len(cell.options))
            least_entropy = lambda cell: len(cell.options) == len(cells[0].options)
            cells = list(filter(lambda cell: not cell.collapsed, cells))
            cells = list(filter(least_entropy, cells))
            if len(cells) == 0:
                self.full = True
            else:
                # Pick a cell and collapse it
                cell = random.choice(cells)
                cell.collapsed = True
                pick = random.choice(list(cell.options))
                cell.options = [pick]
                # Update remaining cells
                for i in range(self.dim):
                    for j in range(self.dim):
                        self.update_cell(i,j)

    def draw(self,canvas):
        for i in range(self.dim):
            for j in range(self.dim):
                cell = self.cells[i * self.dim + j]
                if cell.collapsed and not cell.drawn:
                    tile = self.tiles[list(cell.options)[0]]
                    canvas.blit(tile.image, (i*50, j*50))
                    cell.drawn = True

