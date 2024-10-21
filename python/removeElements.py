from typing import List

class Solution: 
  def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    n = len(nums)

    while i < n:
      if nums[i] == val:
        nums[i] = nums[n - 1] # remove current element by overwriting with the last element 
        n -= 1
      else: 
        i += 1 
    return n 
  
# Initialize the array and value to remove
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

# Create an instance of Solution and call the method
solution = Solution()
new_length = solution.removeElement(nums, val)

# Print the result
print("New length:", new_length)
print("Modified array:", nums[:new_length])

# Time Complexity: O(n) because we're just moving i forward and n backwards
# Space Complexity: O(1): because we're just utilizing two indices.

