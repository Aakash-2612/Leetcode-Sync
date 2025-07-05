class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        temp = -1
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for key, value in d.items():
            if key == value:
                if key > temp:
                    temp = key
            
        return temp
        
