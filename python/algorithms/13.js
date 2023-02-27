/* 
  Array: Mode
  
  Create a function that, given an array of ints,
  returns the int that occurs most frequently in the array.
  What if there are multiple items that occur the same number of time?
    - return all of them (in an array)
    - what if all items occur the same number of times?
      - return empty array
*/

const nums1 = [];
const expected1 = [];

const nums2 = [1];
const expected2 = [1];

const nums3 = [5, 1, 4];
const expected3 = [];

const nums4 = [5, 1, 4, 1];
const expected4 = [1];

const nums5 = [5, 1, 4, 1, 5];
const expected5 = [5, 1];
//  - order doesn't matter

/**
 * Finds the mode or all modes if there are more than one. The mode is the
 *    value which occurs the most times in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Test
 * @returns {Array<number>} Mode or modes in any order.
 */

function mode(nums) {
  const frequency = {};
  let result = [];
  let max = 0;

  for (var i = 0; i < nums.length; i++) {
    const current = nums[i];
    if (!frequency[current]) frequency[current] = 1;
    else frequency[current] += 1;
  }

  for (const entry in frequency) {
    if (frequency[entry] > max) max = frequency[entry];
  }

  for (const entry in frequency) {
    if (frequency[entry] === max) result.push(entry);
  }

  //   for (var i = 0; i < result.length; i++) {
  //     if (result[i + 1] === undefined) break;
  //     if (result[i] !== result[i + 1]) return [];
  //   }

  return result;
}

console.log(mode(nums5));
