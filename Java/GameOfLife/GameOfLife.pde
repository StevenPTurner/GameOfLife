Grid grid;
Debugger debug;
final String format = "HH:mm:ss:SSSSSSSSS";

void setup() {
  size(500,500);
  frameRate(1);
  grid = new Grid(50,50,10);
  debug = new Debugger();
}

void draw() {
  background(0);
  System.out.println(debug.getTimestamp(format));
  run();
  grid.render();
  // System.out.println(debug.getTimestamp(format));
}

private int countPopulation(int i, int j) {
  int populationCount = 0;

  if (i-1 != -1)
    if (grid.isAlive(i-1,j))
      populationCount++;

  if (i-1 != -1 && j-1 != -1)
    if (grid.isAlive(i-1,j-1))
      populationCount++;

  if (j-1 != -1)
    if (grid.isAlive(i,j-1))
      populationCount++;

  if (i+1 != grid.getWidth() && j-1 != -1)
    if (grid.isAlive(i+1,j-1))
      populationCount++;

  if (i+1 != grid.getWidth())
    if (grid.isAlive(i+1,j))
      populationCount++;

  if (i+1 != grid.getWidth() && j+1 != grid.getHeight())
    if (grid.isAlive(i+1,j+1))
      populationCount++;

  if(j+1 != grid.getHeight())
    if(grid.isAlive(i,j+1))
      populationCount++;

  if(i-1 != -1 && j+1 != grid.getHeight())
    if(grid.isAlive(i-1,j+1))
      populationCount++;

  return populationCount;
}

private void run() {
  for(int i=0; i<grid.getWidth(); i++) {
    for(int j=0; j<grid.getHeight(); j++) {
      int count = countPopulation(i,j);

      if (grid.isAlive(i,j) == true)
        if (count < 2 || count > 3)
          grid.kill(i,j);

      if (grid.isAlive(i,j) == false)
        if (count == 3)
          grid.revive(i,j);
    }
  }

}
