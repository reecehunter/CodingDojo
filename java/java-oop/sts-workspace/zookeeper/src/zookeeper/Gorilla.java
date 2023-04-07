package zookeeper;

public class Gorilla extends Mammal {
	public Gorilla() {
		super();
	}
	
	public void throwSomething() {
		System.out.println("Thrown something. -5 Energy");
		energy -= 5;
	}
	
	public void eatBananas() {
		System.out.println("Ate bananas. +10 Energy");
		energy += 10;
	}
	
	public void climb() {
		System.out.println("Climbed. -10 Energy");
		energy -= 10;
	}
}
