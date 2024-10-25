from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_counts = [0] * (n + 1)

        for c in citations:
            paper_counts[min(n, c)] += 1
        
        h = n
        papers = paper_counts[n]

        while papers < h:
            h -= 1
            papers += paper_counts[h]

        return h
    
solution = Solution()

nums1 = [5, 1, 2, 8, 9, 3]
print(solution.hIndex(nums1))  

#Time O(n) because the function iterates through the citation array just once.
#Space O(n) because the function uses an array paper_counts of size n + 1 to store counts for each possible number of citations up to n.