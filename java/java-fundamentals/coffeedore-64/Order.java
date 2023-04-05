import java.util.ArrayList;

public class Order {
    private String name;
    private boolean ready;
    private ArrayList<Item> items;

    public Order() {
        this.name = "Guest";
        this.ready = false;
        this.items = new ArrayList<Item>();
    }

    public Order(String name) {
        this.name = name;
        this.ready = false;
        this.items = new ArrayList<Item>();
    }

    public Order(String name, boolean ready, ArrayList<Item> items) {
        this.name = name;
        this.ready = ready;
        this.items = items;
    }

    public void addItem(Item item) {
        items.add(item);
    }

    public String getStatusMessage() {
        if(ready) return "Your order is ready.";
        else return "Thank you for waiting. Your order will be ready soon.";
    }

    public double getOrderTotal() {
        double total = 0;
        for(Item item : items)
            total += item.getPrice();
        return total;
    }

    public void display() {
        System.out.printf("Customer name: %s\n", name);
        for(Item item : items)
            System.out.printf("%s - %s\n", item.getName(), item.getPrice());
    }

    public String getName() {
        return this.name;
    }
    public void setName(String name) {
        this.name = name;
    }

    public boolean getReady() {
        return this.ready;
    }
    public void setReady(boolean ready) {
        this.ready = ready;
    }

    public ArrayList<Item> getItems() {
        return this.items;
    }
    public void setItems(ArrayList<Item> items) {
        this.items = items;
    }
}