public class Grid {
  private Cell[][] cell;
  private int width,height;
  private float cellSize;

  public Grid(int width, int height, float cellSize) {
    cell = new Cell[width][height];
    this.width = width;
    this.height = height;
    this.cellSize = cellSize;

    for(int i=0; i<width; i++)
      for(int j=0; j<height; j++)
        cell[i][j] = new Cell(i*cellSize,j*cellSize,cellSize);

    randomise();
  }

  public void render(){
    for(int i=0; i<width; i++)
      for(int j=0; j<height; j++)
        cell[i][j].render();
  }

  public void randomise() {
    for(int i=0; i<width; i++)
      for(int j=0; j<height; j++)
        cell[i][j].alive = Math.random() < 0.5;
  }

}
