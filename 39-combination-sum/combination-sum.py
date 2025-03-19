class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        s = set()
        ans = []
        def backtrack(i, cur):
            if i > target:
                return
            if i == target:
                temp = sorted(cur[:])
                if ''.join(map(str, temp)) not in s:
                    ans.append(cur[:])
                    s.add(''.join(map(str, temp)))
                return
            
            for c in candidates:
                backtrack(i+c, cur + [c])
        backtrack(0, [])
        return ans