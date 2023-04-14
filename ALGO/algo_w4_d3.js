/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

const nums2 = [1];
const expected2 = 1;

const nums3 = [];
const expected3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
// none recursive solution
function sumArr(nums) {
    let sum = 0
    for(let i = 0; i < nums.length; i++){
        sum += nums[i]
    }
    return sum
}

console.log(sumArr(nums1))

//recursive solution

function sumArr(nums){
    //bace case
    if (nums.length < 1){
        return 0;
    }
    // some recursive call
    var val = nums.pop()
    return val + sumArr(nums)
}

console.log(sumArr(num1))
console.log(sumArr(num2))
console.log(sumArr(num3))