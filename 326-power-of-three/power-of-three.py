def sol(n):
    if n < 1:
        return False
    if n == 1.0:
        return True

    return sol(n/3)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return sol(n)