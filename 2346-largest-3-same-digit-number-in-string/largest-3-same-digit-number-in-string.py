class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        arr = [str(x) * 3 for x in range(9, -1, -1)]
        
        for i in arr:
            if i in num:
                return i

        return ""