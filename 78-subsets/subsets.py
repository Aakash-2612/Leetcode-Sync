class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(i, cur):
            if i == len(nums):
                ans.append(cur[:])
                return
            
            backtracking(i+1, cur + [nums[i]])
            backtracking(i+1, cur)
        
        backtracking(0, [])
        return ans