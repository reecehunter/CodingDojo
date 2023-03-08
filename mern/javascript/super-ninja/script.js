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

class Sensei extends Ninja {
  constructor(name, health, speed = 3, strength = 3, wisdom = 10) {
    super(name, health, (speed = 3), (strength = 3));
    this.wisdom = wisdom;
  }

  speakWisdom() {
    console.log(
      "What one programmer can do in one month, two programmers can do in two months."
    );
    return this;
  }
}

const sensei = new Sensei("Reece", 10);
sensei.sayName().showStats().speakWisdom();
