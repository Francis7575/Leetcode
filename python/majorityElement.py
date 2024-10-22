from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else: 
                counter[num] = 1

        max_count = -1
        ans = -1

        for key, val in counter.items():
            if val > max_count:
                max_count = val
                ans = key
        
        return ans
    
nums = [10,8,6,5,1,1,1,2,10,10,10] 
solution = Solution()
majorityNum = solution.majorityElement(nums)

print("Highest frequency:", majorityNum)
# final counter dictionary
# {
#     10: 4,
#     8: 1,
#     6: 1,
#     5: 1,
#     1: 3,
#     2: 1
# }
# Time: O(n) // because i iterated over the list of size n twice, once to populate the dictionary and once to find the majority element.
# Space: O(n) //  because in the worst case, the counter dictionary will store n unique elements from the list.