import java.util.ArrayList;

public class TestOrders {
    public static void main(String[] args) {
        // Kiosk
        CoffeeKiosk kiosk = new CoffeeKiosk();
        kiosk.addMenuItem("Drip Coffee", 2.0);
        kiosk.addMenuItem("Latte", 2.5);
        kiosk.addMenuItem("Cappuccino", 3.0);
        kiosk.newOrder();
    }
}
