class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible = 0
        not_divis = 0

        for i in range(1, n+1):
            if i % m == 0:
                divisible += i
            else:
                not_divis += i

        return not_divis - divisible
            