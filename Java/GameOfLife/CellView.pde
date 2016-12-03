public class CellView {
  private int fillAlive;
  private int fillDead;
  private int strokeColour;
  private float x;
  private float y;
  private float size;

  public CellView(float x, float y, float size) {
    fillAlive = 255;
    fillDead = 0;
    strokeColour = 128;
    this.x = x;
    this.y = y;
    this.size = size;
  }

  public void render(boolean isAlive) {
    if(isAlive)
      fill(fillAlive);
    else
      fill(fillDead);

    stroke(strokeColour);
    rect(x,y,size,size);
  }
}
