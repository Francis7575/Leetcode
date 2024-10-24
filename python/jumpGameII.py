from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0          # This keeps track of the number of jumps made.
        last_int = 0       # This tracks the farthest index reachable in the current jump.
        max_int = 0        # farthest position that can be reach as i progress through the array.

        for i in range(len(nums) - 1):
            max_int = max(max_int, i + nums[i])
            if i == last_int:
                jumps += 1        
                last_int = max_int  
        return jumps
        
# Iteration 1: (i = 0)
# max_int = max(0, 0 + 2) = 2
# last_int = 2
# Iteration 2: (i = 1)
# max_int = max(2, 1 + 3) = 4
# last_int = 4

solution = Solution() 
nums1 = [2,3,1,1,4]
print(solution.jump(nums1))  

#Time: O(n) because i'm just iterating through the array once.
#Space: O(1) because i'm just using a couple of variables that store integers.