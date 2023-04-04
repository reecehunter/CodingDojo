import java.util.HashMap;

public class SongUtils {
  public String getLyrics(HashMap<String,String> songs, String songName) {
    return songName + ": " + songs.get(songName);
  }
}