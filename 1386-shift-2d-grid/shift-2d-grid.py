class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for i in grid:
            for j in i:
                arr.append(j)
        
        s = arr + arr
        r = len(grid[0])
        # print(r)
        pos = len(arr) - (k%len(arr))
        res = s[pos:pos+len(arr)]
        ans = []
        temp =[]
        count = 1
        for i in res:
            if count == r:
                temp.append(i)
                ans.append(temp)
                temp = []
                count = 1
            else:
                count += 1
                temp.append(i)
        
        return ans