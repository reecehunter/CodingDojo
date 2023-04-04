public class Puzzling {
  public static void main(String[] args) {
    PuzzleJava puzzleJava = new PuzzleJava();

    System.out.println("----- Get Ten Rolls -----");
    int[] rolls = puzzleJava.getTenRolls();
    for(int roll : rolls) {
      System.out.println(roll);
    }
    System.out.println("\n");

    System.out.println("----- Get Random Letter -----");
    System.out.println(puzzleJava.getRandomLetter());
    System.out.println("\n");

    System.out.println("----- Generate Password -----");
    System.out.println(puzzleJava.generatePassword());
    System.out.println("\n");

    System.out.println("----- Get New Password Set -----");
    String[] passwords = puzzleJava.getNewPasswordSet(3);
    for(String password : passwords) {
      System.out.println(password);
    }
    System.out.println("\n");
  }
}