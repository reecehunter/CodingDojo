import java.util.Random;

public class PuzzleJava {
  public int[] getTenRolls() {
    int[] result = new int[10];
    Random randMachine = new Random();

    for(int i = 0; i < 10; i++) {
      result[i] = randMachine.nextInt(20);
    }

    return result;
  }

  public char getRandomLetter() {
    Random randMachine = new Random();
    char[] alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    int randNum = randMachine.nextInt(25);
    return alphabet[randNum];
  }

  public String generatePassword() {
    String password = "";

    for(int i = 0; i < 8; i++) {
      password += this.getRandomLetter();
    }

    return password;
  }

  public String[] getNewPasswordSet(int amount) {
    String[] passwords = new String[amount];

    for(int i = 0; i < amount; i++) {
      String password = this.generatePassword();
      passwords[i] = password;
    }

    return passwords;
  }
}