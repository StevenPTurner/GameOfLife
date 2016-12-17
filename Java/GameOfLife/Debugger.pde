import java.util.Date;
import java.text.SimpleDateFormat;

class Debugger {
  boolean recording;

  public Debugger() {
    recording = false;
  }

  public Date getTimestamp() {
    Date timestamp = new Date();
    return timestamp;
  }

  public String getTimestamp(String formatString) {
    Date dateNow = new Date();
    SimpleDateFormat timestamp = new SimpleDateFormat(formatString);
    return timestamp.format(dateNow);
  }

  public void start() {

  }

  public void stop() {

  }

  private void writeToDatabase() {

  }

  private String calculateTimeDifference(){

  }

}
