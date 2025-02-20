class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s = '01'
        sett = set(nums)

        def backtracking(i, cur):
            if i == n:
                if cur not in sett:
                    return cur
                return ''
            
            for c in s:
                ans = backtracking(i+1, cur+c)
                if ans:
                    return ans
        
        return backtracking(0, '')