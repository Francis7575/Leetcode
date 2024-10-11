const twoSum = (nums, target) => {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    let nums1 = nums[i] // get all the numbers on the array
    let nums2 = target - nums1 
    if (map.has(nums2)) {
      return [i, map.get(nums2)] // breaks down the for loop after getting the target result
    }
    map.set(nums1, i)
  }
};

// the result Is [7, 4] because when iterating the number 2 it identifies that the number 8 was previously iterated 
// and 8 + 2 = 10 which matches the target's value
const result = twoSum([1, 3, 3, 5, 8, 4, 3, 2, 5], 10)
console.log(result)