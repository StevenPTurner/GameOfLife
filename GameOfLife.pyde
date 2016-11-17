class Node(object):

    def __init__(self, x, y, size):
        self.is_alive = false;
        self.population_count = 0;
        self.x = x
        self.y = y
        self.size = size

class NodeView(object):

    def __init__(self, x, y, size):
        self.fill_alive = 255;
        self.fill_dead = 0;
        self.stroke_colour = 128;
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
     

           
def setup():
    size(500,500)
    

def draw():
    background(0)
    node_view = NodeView(10,10,50)
    node_view.render(False)