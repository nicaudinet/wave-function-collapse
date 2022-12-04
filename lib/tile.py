from pygame.transform import rotate

class Tile:
    def __init__(self, image, edges):
        self.image = image
        self.edges = edges
        self.neighbors = [set(), set(), set(), set()]
        self.up = self.neighbors[0]
        self.right = self.neighbors[1]
        self.down = self.neighbors[2]
        self.left = self.neighbors[3]

    def analyze(self, tiles):
        for i, tile in enumerate(tiles):
            for j in range(4):
                if self.edges[j] == tile.edges[(j+2) % 4]:
                    self.neighbors[j].add(i)
