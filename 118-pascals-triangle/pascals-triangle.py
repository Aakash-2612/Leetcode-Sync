class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        k = 1
        while k != numRows+1:
            carry = 0
            temp = []
            for i in range(k-1):
                temp.extend([ans[-1][i] + carry])
                carry = ans[-1][i]
            if carry != 0:
                temp.extend([carry])
            
            if len(temp) != k:
                temp = [1] * k
            ans.append(temp)
            k += 1
        
        return ans