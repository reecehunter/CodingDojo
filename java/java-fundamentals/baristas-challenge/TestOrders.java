import java.util.ArrayList;

public class TestOrders {
    public static void main(String[] args) {
        // Menu items
        Item item1 = new Item("Drip Coffee", 2.0);
        Item item2 = new Item("Latte", 2.5);
        Item item3 = new Item("Mocha", 3.5);
        Item item4 = new Item("Cappuccino", 4.0);
    
        // Unspecified Orders
        Order order1 = new Order();
        Order order2 = new Order();

        // Overloaded Orders 1
        Order order3 = new Order("Billy");
        Order order4 = new Order("Bob");
        Order order5 = new Order("Joe");

        // Overloaded Orders 2
        Order order6 = new Order("Billy");
        order6.addItem(item1);
        order6.addItem(item2);
        Order order7 = new Order("Bob");
        order7.addItem(item1);
        order7.addItem(item3);
        Order order8 = new Order("Joe");
        order8.addItem(item2);
        order8.addItem(item4);

        // Tests
        order1.setReady(true);
        System.out.println(order1.getStatusMessage());
        System.out.println(order6.getOrderTotal());
        order6.display();
    }
}
