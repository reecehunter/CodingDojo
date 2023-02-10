/* 
    Zip Arrays into Map

    Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.
    Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

const keys2 = [];
const vals2 = [];
const expected2 = {};

const keys4 = ["abc", 3, "yo", 'something'];
const vals4 = [42, "wassup", true];

const keys5 = ["abc", 3, "yo"];
const vals5 = [42, "wassup", true, 'something'];

function zip(keys, values) {
    if(keys.length <= values.length) return false;
    var result = {};
    for(var i = 0; i < keys.length; i++) {
        result[keys[i]] = values[i]
    }
    return result;
}

console.log(zip(keys4, vals4));

// ****************** Potential Edge Cases *************************
// Can you have a bool as a key??

const keys3 = ["abc", 3, "yo", true];
const vals3 = [42, "wassup", true, 5];
const expected3 = '?'

// const keys4 = ["abc", 3, "yo", 'something'];
// const vals4 = [42, "wassup", true];

const expected4 = {
abc: 42,
3: "wassup",
yo: true,
something: undefined
};

// const keys5 = ["abc", 3, "yo"];
// const vals5 = [42, "wassup", true, 'something'];
const expected5 = false


/* 
    Invert Hash
    A hash table / hash map is an obj / dictionary
    Given an object / dict,
    return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const two_obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const two_expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

// ****************** Potential Edge Cases *************************

const two_obj2 = { name: "Zaphod", charm: "high", morals: "dicey", something:"dicey" };
const two_expected2 = { Zaphod: "name", high: "charm", dicey: ["morals", "something"] };
const two_expected3 = { Zaphod: "name", high: "charm", dicey: "morals", dicey2: "something" };

/**
    * Inverts the given object's key value pairs so that the original values
    * become the keys and the original keys become the values.
    * - Time: O(?).
    * - Space: O(?).
    * @param {Object<string, any>} obj
    * @return The given object with key value pairs inverted.
*/
function invertObj(obj) {}