class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            c = 0
            if n <= 1:
                return False
            for i in range(2, int(n**(1/2))+1):
                if n % i == 0:
                    c += 1
            if c == 0:
                return True
            return False
        
        count = 0
        for j in range(left, right+1):
            b = bin(j)[2:]
            n = b.count('1')
            # print(n)
            if isPrime(n):
                count += 1
        
        return count