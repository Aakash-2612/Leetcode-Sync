class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def fun(n):
            count = 0
            for i in range(1, len(n)-1):
                if int(n[i-1]) < int(n[i]) > int(n[i+1]):
                    count += 1
                elif int(n[i-1]) > int(n[i]) < int(n[i+1]):
                    count += 1

            return count

        ans = 0
        for i in range(num1, num2+1):
            ans += fun(str(i))

        return ans