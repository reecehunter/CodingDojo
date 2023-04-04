import java.util.ArrayList;

public class CafeUtil {
  public int getStreakGoal(int weeks) {
    int sum = 0;

    for(int i = 0; i <= weeks; i++)
      sum += i;
    
    return sum;
  }

  public double getOrderTotal(double[] prices) {
    double sum = 0;

    for(double price : prices)
      sum += price;

    return sum;
  }

  public void displayMenu(ArrayList<String> menuItems) {
    for(String item : menuItems) {
      System.out.println(item);
    }
  }

  public void addCustomer(ArrayList<String> customers) {
    System.out.println("Please enter your name:");
    String username = System.console().readLine();
    System.out.printf("Hello, %s.\n", username);
    customers.add(username);
    System.out.println(customers);
  }

  public void printPriceChart(String product, double price, int maxQuantity) {
    System.out.println(product);
    for(int i = 1; i <= maxQuantity; i++) {
      System.out.printf("%s - $%s\n", i, price * i);
    }
  }
}