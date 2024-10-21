from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1

        for i in range(1, n):
          if nums[i] != nums[i - 1]: # when is not a duplicate number  
            nums[j] = nums[i]
            j += 1

        return j 

nums = [0,0,1,1,1,2,2,3,3,4] 

solution = Solution()
new_length = solution.removeDuplicates(nums)

print("New length:", new_length)
print("Modified array:", nums[:new_length])

# because i'm only setting two indices through the array 
#Time O(n) 
#Space O(1) 