
public class Driver extends Car {
	public Driver() {
		super();
	}
	
	public void drive() {
		gas -= 1;
		System.out.println("Drive: -1 gas");
	}
	
	public void boost() {
		gas -= 3;
		System.out.println("Boost: -1 gas");
	}
	
	public void refuel() {
		gas += 2;
		System.out.println("Refuel: +2 gas");
	}
}
