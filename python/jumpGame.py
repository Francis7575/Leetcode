from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
      farthest = 0
      last = len(nums) - 1
      for i in range(len(nums)):
        if i > farthest:
          return False
        if nums[i] + i > farthest:  
          farthest = nums[i] + i
        if farthest >= last:
          return True

# Example Usage
solution = Solution()

nums1 = [2, 3, 1, 1, 4]
print(solution.canJump(nums1))  # Output: True

nums2 = [1, 1, 0, 0, 4]
print(solution.canJump(nums2))  # Output: False

# Time complexity: O(n) (single pass through the list).
# Space complexity: O(1) (constant space usage).