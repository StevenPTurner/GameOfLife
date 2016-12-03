public class Cell {
  private float x,y,size;
  private boolean alive;
  private CellView view;
  private int populationCount;

  public Cell(float x, float y, float size) {
    this.x = x;
    this.y = y
    this.size = size;
    alive = false;
    view = new CellView(x,y,size)
  }

  public kill() {
    alive = false;
  }

  public revive() {
    alive = true;
  }

  public render() {
    view.render(alive);
  }

}
