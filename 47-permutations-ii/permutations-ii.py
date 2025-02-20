class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        d = Counter(nums)

        def backtracking(i, cur):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return
            
            for c in d:
                if d[c]:
                    d[c] -= 1
                    backtracking(i+1, cur + [c])
                    d[c] += 1
        
        backtracking(0, [])
        return ans