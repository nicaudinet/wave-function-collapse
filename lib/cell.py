class Cell:
    def __init__(self):
        self.collapsed = False
        self.options = set(range(5))
        self.drawn = False
