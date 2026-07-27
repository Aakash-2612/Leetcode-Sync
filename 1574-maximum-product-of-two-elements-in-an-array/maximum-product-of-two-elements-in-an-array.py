class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        secondMax = temp
        for i in nums:
            if i >= temp: # 5>5
                secondMax = temp #5
                temp = i #5
            # i = 5
            if i > secondMax and i != temp: 
                secondMax = i # 4
        
        # print(temp)
        # print(secondMax)

        return (temp-1)*(secondMax-1)
