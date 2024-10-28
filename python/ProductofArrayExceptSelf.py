class Solution:
    def productExceptSelf(self, nums):
      n = len(nums)
      answer = [1] * n  

      left_product = 1
      for i in range(n):
          answer[i] = left_product
          left_product *= nums[i]

      right_product = 1
      for i in range(n - 1, -1, -1):
          answer[i] *= right_product
          right_product *= nums[i]

      return answer

solution = Solution()
nums = [1,2,3,4]
print(solution.productExceptSelf(nums))  

# Time: O(n) because i iterate through the list twice once for the left products and once for the right products.
# Space: O(1) because constant space was used for left_product and right_product.