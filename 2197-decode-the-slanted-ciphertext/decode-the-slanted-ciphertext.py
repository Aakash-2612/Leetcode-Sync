class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        l = len(encodedText)
        r = l//rows
        # print(r)
        arr = []
        temp = []
        for i in range(l):
            temp.append(encodedText[i])
            if (i+1) % r == 0:
                arr.append(temp)
                temp = []
    
        # print(arr)
        ans = ''
        i, j = 0, 0
        for k in range(r):
            j = k
            i = 0
            while i < rows and j < r:
                ans += arr[i][j]
                i += 1
                j += 1
        
        return ans.rstrip()