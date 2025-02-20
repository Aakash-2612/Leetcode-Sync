class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sett = set()

        def backtracking(i, cur):
            if i == len(nums):
                ans.append(cur[:])
                return
            
            for c in nums:
                if c not in sett:
                    cur.append(c)
                    sett.add(c)
                    backtracking(i+1, cur)
                    cur.pop()
                    sett.remove(c)
        
        backtracking(0, [])
        return ans