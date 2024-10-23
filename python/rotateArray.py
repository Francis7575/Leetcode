from typing import List

#  Do not return anything, modify nums in-place instead.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
      x = k%len(nums)

      def rev(s, e):
        while s<e:
            nums[s], nums[e] = nums[e], nums[s]
            s+=1
            e-=1
        
      nums.reverse()
      rev(0, x-1) # indices to reverse k numbers
      rev(x, len(nums)-1) # indices to reverse rest of numbers

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

solution = Solution()
solution.rotate(nums, k)  # Rotate the array in place

print("Rotated array:", nums)  # Print the result

# Original Array: [1, 2, 3, 4, 5, 6, 7], k = 3
# 1. Reverse entire array: [7, 6, 5, 4, 3, 2, 1]
# 2. Reverse first 3 elements: [5, 6, 7, 4, 3, 2, 1]
# 3. Reverse remaining elements: [5, 6, 7, 1, 2, 3, 4]
# Rotated array: [5, 6, 7, 1, 2, 3, 4]

# Time Complexity: O(n): Because all operations involve iterating through the array, resulting in linear time complexity.
# Space Complexity: O(1): Because the algorithm modifies the input array directly and only uses a constant amount of additional space.