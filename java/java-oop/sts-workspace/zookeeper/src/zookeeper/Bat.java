package zookeeper;

public class Bat extends Mammal {
	public Bat() {
		energy = 300;
	}
	
	public void fly() {
		System.out.println("Fly. -50 Energy");
		energy -= 50;
	}
	
	public void eatHumans() {
		energy += 25;
	}
	
	public void attackTown() {
		System.out.println("Attacked town. -100 Energy");
		energy -= 100;
	}
}
