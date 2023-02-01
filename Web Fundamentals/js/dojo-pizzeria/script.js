function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

function printAssignmentPizzas() {
    console.log(pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]));
    console.log(pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]));
    console.log(pizzaOven("deep dish", "traditional", ["mozzarella"], ["ham", "pineapple"]));
    console.log(pizzaOven("hand tossed", "traditional", ["mozzarella"], ["squid", "jellybeans"]));    
}

function printRandomPizza() {
    const crusts = ["Thin", "New York", "St. Louis", "Thick"];
    const sauces = ["Marinera", "Sweet tomato", "Vodka", "White"];
    const cheeses = ["Mozzarella", "Cheddar", "Colby", "Provolone"];
    const toppings = ["Pepperoni", "Olives", "Pineapple", "Bacon"];

    const crustIndex = Math.round(Math.random() * 3);
    const sauceIndex = Math.round(Math.random() * 3);
    const cheeseIndex = Math.round(Math.random() * 3);
    const toppingIndex = Math.round(Math.random() * 3);

    return pizzaOven(crusts[crustIndex], sauces[sauceIndex], cheeses[cheeseIndex], toppings[toppingIndex]);
}

console.log(printRandomPizza());