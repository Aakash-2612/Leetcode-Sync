class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        left = []
        product = 1
        for i in range(n):
            left.append(product)
            product = product * nums[i]

        right = [0] * n
        product = 1
        for i in range(n - 1, -1, -1):
            right[i] = product
            product = product * nums[i]

        result = []
        for i in range(n):
            result.append(left[i] * right[i])

        return result
