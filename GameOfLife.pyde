class CellView(object):

    def __init__(self, x, y, size):
        self.fill_alive = 255
        self.fill_dead = 0
        self.stroke_colour = 128
        self.x = x
        self.y = y
        self.size = size

    def render(self, is_alive):
        stroke(self.stroke_colour)
        if is_alive:
            fill(self.fill_alive)
        else:
            fill(self.fill_dead)
        rect(self.x, self.y, self.size, self.size)

class Cell(object):

    def __init__(self, x, y, size):
        self.is_alive = False
        self.population_count = 0
        self.x = x
        self.y = y
        self.size = size
        self.view = CellView(self.x, self.y, self.size)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def kill(self):
        self.is_alive = False

    def revive(self):
        self.is_alive = True

    def render(self):
        for i in range(self.size):
            for j in range(self.size):
                self.view.render(True)

class Grid(object):

    def __init__(self, size):
        self.size = size
        self.grid = []
        for i in range(self.size):
            self.grid.append([])
            for j in range(self.size):
                temp = Cell((i*25), (j*25), self.size)
                self.grid[i].append(temp)

    def render(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j].render()


def setup():
    size(500,500)

def draw():
    background(0)
    c = Grid(20)
    c.render()
