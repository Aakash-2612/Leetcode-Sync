class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        
        power = 1
        while power <= n:
            if power == n:
                return True
            power = power * 2
        return False