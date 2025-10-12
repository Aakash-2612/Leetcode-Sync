def sol(n):
    if n < 1:
        return False
    if n == 1.0:
        return True
    if n%4 != 0:
        return False
        
    return sol(n/4)

class Solution(object):
    def isPowerOfFour(self, n):
        return sol(n)