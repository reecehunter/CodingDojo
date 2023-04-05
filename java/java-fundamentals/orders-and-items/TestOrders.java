import java.util.ArrayList;

public class TestOrders {
    public static void main(String[] args) {
        // Menu items
        Item item1 = new Item("Drip Coffee", 2.0);
        Item item2 = new Item("Latte", 2.5);
        Item item3 = new Item("Mocha", 3.5);
        Item item4 = new Item("Cappuccino", 4.0);
    
        // Order variables -- order1, order2 etc.
        ArrayList<Item> cindhuriItems = new ArrayList<>();
        items.add(item1);
        Order order1 = new Order("Cindhuri", 2.0, true, items);


        ArrayList<Item> jimmyItems = new ArrayList<>();
        items.add(item1);
        Order order2 = new Order("Jimmy", 2.0, true, items);

        ArrayList<Item> noahItems = new ArrayList<>();
        items.add(item4);
        Order order3 = new Order("Noah", 4.0, false, items);

        ArrayList<Item> samItems = new ArrayList<>();
        items.add(item2);
        items.add(item2);
        items.add(item2);
        Order order4 = new Order("Sam", 7.5, false, items);
    
        // Application Simulations
        // Use this example code to test various orders' updates
        System.out.printf("Name: %s\n", order1.name);
        System.out.printf("Total: %s\n", order1.total);
        System.out.printf("Ready: %s\n", order1.ready);
    }
}
