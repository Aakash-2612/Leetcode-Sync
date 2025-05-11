import numpy as np
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        temp = False
        count = 0
        for i in arr:
            if count == 3:
                return True
            if i%2 != 0:
                count += 1
                temp= True
            elif i%2 == 0:
                temp = False
                count = 0
        if temp and count == 3:
            return True
        else:
            return False
            