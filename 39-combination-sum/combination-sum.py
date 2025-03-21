class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr = sorted(set(arr))
        ans = []

        def backtrack(i, cur, start):
            if i == target:
                ans.append(cur[:])
                return

            for j in range(start, len(arr)):
                if i + arr[j] > target:
                    break
                backtrack(i + arr[j], cur + [arr[j]], j)
            
        backtrack(0, [], 0)
        return ans