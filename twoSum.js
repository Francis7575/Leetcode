// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

// Example 1:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

// Example 2:
// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]

const twoSum = (nums, target) => {
  let map = new Map(); // Initialize the Map to store numbers and their indices
  for (let i = 0; i < nums.length; i++) { // Iterate through each number
    let nums1 = nums[i] // Current number
    let nums2 = target - nums1  // Complement needed to reach target
    if (map.has(nums2)) { // Check if the complement exists in the Map
      return [i, map.get(nums2)] // // Return the current index and index of complement
    }
    map.set(nums1, i) // Store the current number with its index in the Map
  }
};

// the result Is [7, 4] because when iterating the number 2 it identifies that the number 8 was previously iterated 
// and 8 + 2 = 10 which matches the target's value
const result = twoSum([1, 3, 3, 5, 8, 4, 3, 2, 5], 10)
console.log(result)

// Time complexity:
// the time complexity is O(n) for iterating through the array and performing constant-time operations with the Map.

// Space complexity:
// The space complexity is linear, O(n), as the Map may need to accommodate up to n distinct numbers based on the input array.