// 1
var hello = "world";
console.log(hello);
// world

// 2
var needle = "haystack";
function test() {
  var needle = "magnet";
  console.log(needle);
}
test();
// magnet

// 3
var brendan = "super cool";
function print() {
  brendan = "only okay";
  console.log(brendan);
}
console.log(brendan);
// only okay
// only okay

// 4
var food = "chicken";
console.log(food);
function eat() {
  food = "half-chicken";
  console.log(food);
  var food = "gone";
}
eat();
// chicken
// half-chicken

// 5
var mean = function () {
  food = "chicken";
  console.log(food);
  var food = "fish";
  console.log(food);
};
mean();
console.log(food);
console.log(food);
// chicken
// chicken

// 6
console.log(genre);
var genre = "disco";
function rewind() {
  genre = "rock";
  console.log(genre);
  var genre = "r&b";
  console.log(genre);
}
rewind();
console.log(genre);
// undefined
// rock
// r&b
// disco

// 7
dojo = "san jose";
console.log(dojo);
function learn() {
  dojo = "seattle";
  console.log(dojo);
  var dojo = "burbank";
  console.log(dojo);
}
learn();
console.log(dojo);
// San Jose
// seattle
// burbank
// san jose
