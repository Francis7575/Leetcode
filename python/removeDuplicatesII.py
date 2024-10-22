from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        count = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1 
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j

nums = [0,0,0,0,1,1,1,2,3,3,4] 

solution = Solution()
new_length = solution.removeDuplicates(nums)

print("New length:", new_length)
print("Modified array:", nums[:new_length])

#Time O(n) because i'm just moving i and j through the array.
#Space O(1) because i'm just using a couple of indices and a count variable.
            