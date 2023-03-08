class Card {
  constructor(name, cost) {
    this.name = name;
    this.cost = cost;
  }
}

class Unit extends Card {
  constructor(name, cost, power, resilience) {
    super(name, cost);
    this.power = power;
    this.resilience = resilience;
  }

  attack(target) {
    target.resilience -= this.power;
    console.log(`${target.name}'s resilience was reduced by ${this.power}.`);
    return this;
  }
}

class Effect extends Card {
  constructor(name, cost, text, stat, magnitude) {
    super(name, cost);
    this.text = text;
    this.stat = stat;
    this.magnitude = magnitude;
  }

  play(target) {
    target[this.stat] -= this.magnitude;
    console.log(
      `${target.name}'s ${this.stat} was reduced by ${this.magnitude}.`
    );
    return this;
  }
}

const redBeltNinja = new Unit("Red Belt Ninja", 3, 3, 4);
const blackBeltNinja = new Unit("Black Belt Ninja", 4, 5, 4);

const hardAlgorithm = new Effect(
  "Hard Algorithm",
  2,
  "Increase target's resilience by 3",
  "resilience",
  3
);
const unhandledPromiseRejection = new Effect(
  "Unhandled Promise Rejection",
  2,
  "Reduce target's resilience by 2",
  "resilience",
  3
);
const pairProgramming = new Effect(
  "Pair Programming",
  2,
  "Increase target's power by 2",
  "power",
  3
);

hardAlgorithm.play(redBeltNinja);
unhandledPromiseRejection.play(blackBeltNinja);
pairProgramming.play(redBeltNinja);
redBeltNinja.attack(blackBeltNinja);
