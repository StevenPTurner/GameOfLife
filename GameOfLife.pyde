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
        self.is_alive = True
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
                self.view.render(self.is_alive)

class Grid(object):

    def __init__(self, node_size, grid_size):
        self.node_size = node_size
        self.grid = []
        self.grid_size = grid_size
        for i in range(self.grid_size):
            self.grid.append([])
            for j in range(self.grid_size):
                temp = Cell((i*self.node_size), (j*self.node_size), self.node_size)
                self.grid[i].append(temp)

    def render(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.grid[i][j].render()

    def is_alive(self,i,j):
        return self.grid[i][j].is_alive

def setup():
    size(500,500)
    #frameRate(60)

def draw():
    background(0)
    c = Grid(20,25)
    for i in range(len(c.grid)):
        for j in range(len(c.grid[0])):
            print count_population(c,5,5)
    c.render()

def count_population(grid,i,j):
    population_count = 0

    if (i-1 != -1):
        if grid.is_alive(i-1,j):
            population_count+=1

    if (i-1 != -1 and j-1 != -1):
        if grid.is_alive(i-1,j-1):
            population_count+=1

    if (j-1 != -1):
        if grid.is_alive(i,j-1):
            population_count+=1

    if (i+1 != len(grid.grid) and j-1 != -1):
        if grid.is_alive(i+1,j-1):
            population_count+=1

    if (i+1 != len(grid.grid)):
        if grid.is_alive(i+1,j):
            population_count+=1

    if (i+1 != len(grid.grid) and j+1 != len(grid.grid[0])):
        if grid.is_alive(i+1,j+1):
            population_count+=1

    if(j+1 != len(grid.grid[0])):
        if(grid.is_alive(i,j+1)):
            population_count+=1

    if(i-1 != -1 and j+1 != len(grid.grid[0])):
        if(grid.is_alive(i-1,j+1)):
            population_count+=1

    return population_count
