import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class GameOfLife extends PApplet {

Grid grid;

public void setup() {
  
  frameRate(2);

  grid = new Grid(50,50,10);
  // System.out.println(grid.getWidth());
  // System.out.println(grid.getHeight());
  System.out.println(countPopulation(5,5));
}

public void draw() {
  background(0);
  run();
  grid.render();
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

  public boolean isAlive(int row, int column) {
    return cell[row][column].isAlive();
  }

  public void render(){
    for(int i=0; i<width; i++)
      for(int j=0; j<height; j++)
        cell[i][j].render();
  }

  public void randomise() {
    for(int i=0; i<width; i++)
      for(int j=0; j<height; j++)
        cell[i][j].alive = Math.random() < 0.5f;
  }

  public int getWidth() {
    return width;
  }

  public int getHeight() {
    return height;
  }

  public void kill(int i, int j) {
    cell[i][j].kill();
  }

  public void revive(int i, int j) {
    cell[i][j].revive();
  }

}
  public void settings() {  size(500,500); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "GameOfLife" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
