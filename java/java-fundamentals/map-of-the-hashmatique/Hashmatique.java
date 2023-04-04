import java.util.HashMap;

public class Hashmatique {
  public static void main(String[] args) {
    SongUtils songUtils = new SongUtils();

    HashMap<String, String> songs = new HashMap<String, String>();
    songs.put("song1", "lyrics1");
    songs.put("song2", "lyrics2");
    songs.put("song3", "lyrics3");
    songs.put("song4", "lyrics4");

    System.out.println(songUtils.getLyrics(songs, "song2"));
  }
}