class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        s = set()
        nums.sort()

        def backtracking(i, cur):
            if i >= len(nums):
                temp = ''.join(str(j) for j in cur)
                if temp not in s:
                    ans.append(cur[:])
                    s.add(temp)
                return
            
            backtracking(i+1, cur)
            backtracking(i+1, cur + [nums[i]])
            
        backtracking(0, [])
        return ans
