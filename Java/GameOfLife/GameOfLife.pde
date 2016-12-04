Grid grid;

void setup() {
  size(500,500);
  frameRate(24);

  grid = new Grid(50,50,10);
}

void draw() {
  background(0);
  grid.render();
}
