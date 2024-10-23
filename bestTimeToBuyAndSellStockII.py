from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        low = prices[0]
        high = prices[0]
        profit = 0  
        n = len(prices)

        while i < n -1:
            #look where to buy
            while i < n - 1 and prices[i] > prices[i + 1]:
                i += 1
            low = prices[i]

            #look where to sell
            while i < n - 1 and prices[i] <= prices[i+ 1]:
                i += 1
            high = prices[i]
            profit += high - low

        return profit
    
prices = [7,1,5,3,6,4]
solution = Solution()
profit = solution.maxProfit(prices) 
print("Profit:", profit)  # Print the result

# Time: O(n) because all the while loops are working together to push i through the array once.
# Space: O(1) because i'm using just a few variables.

