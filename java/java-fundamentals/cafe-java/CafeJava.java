public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly. ";
        String readyMessage = ", your order is ready. ";
        String displayTotalMessage = "Your total is $";
        
        // Menu variables (add yours below)
        double mochaPrice = 3.5;
        double dripPrice = 1.5;
        double lattePrice = 2.5;
        double cappuccinoPrice = 3.0;
    
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Noah";
        String customer3 = "Sam";
        String customer4 = "Jimmy";
    
        // Order completions (add yours below)
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = true;
        boolean isReadyOrder4 = true;
    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        // System.out.println(generalGreeting + customer1); // Displays "Welcome to Cafe Java, Cindhuri"
    	// ** Your customer interaction print statements will go here ** //
        System.out.println(customer1 + pendingMessage);
        System.out.println(customer2 + readyMessage + (isReadyOrder2 ? (displayTotalMessage + cappuccinoPrice) : "."));
        System.out.println(customer3 + (isReadyOrder3 ? readyMessage : pendingMessage) + displayTotalMessage + lattePrice*2);
        // System.out.println(customer4 + readyMessage);
    }
}
