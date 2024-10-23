from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
    
prices = [7,1,5,3,10,4]

solution = Solution()
max_profit = solution.maxProfit(prices) # Rotate the array in place
print("Max profit:", max_profit)  # Print the result

# Time: O(n) because it just a loop through the array once.  
# Space: O(1) because i'm using just a few variables.