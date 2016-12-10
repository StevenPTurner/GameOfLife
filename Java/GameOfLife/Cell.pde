public class Cell {
  private float x,y,size;
  private boolean alive;
  private CellView view;
  private int populationCount;

  public Cell(float x, float y, float size) {
    this.x = x;
    this.y = y;
    this.size = size;
    alive = false;
    view = new CellView(x,y,size);
  }

  public void kill() {
    alive = false;
  }

  public void revive() {
    alive = true;
  }

  public void render() {
    view.render(alive);
  }

  public boolean isAlive() {
    return alive;
  }

}
