class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        neg = []
        temp = nums[-1] * nums[-2] * nums[-3]
        for i in nums:
            if i < 0:
                neg.append(i)
        
        if len(neg) >= 2:
            a, b = neg[0], neg[1]
            c = nums[-1]
            res = a * b * c
            return max(temp, res)
        else:
            return temp