class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count1 = 0
        for i in range(len(s)):
            if i % 2 == 0 and s[i] != "1":
                count1 += 1
            elif i % 2 != 0 and s[i] != "0":
                count1 += 1

        return min(count1, len(s) - count1)