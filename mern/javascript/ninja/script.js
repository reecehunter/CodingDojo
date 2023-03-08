class Ninja {
  constructor(name, health, speed = 3, strength = 3) {
    this.name = name;
    this.health = health;
    this.speed = speed;
    this.strength = strength;
  }

  sayName() {
    console.log(this.name);
    return this;
  }

  showStats() {
    console.log(this.speed, this.strength);
    return this;
  }

  drinkSake() {
    this.health += 10;
    console.log(this.health);
    return this;
  }
}

const ninja = new Ninja("Reece", 10);
ninja.sayName().showStats().drinkSake();
