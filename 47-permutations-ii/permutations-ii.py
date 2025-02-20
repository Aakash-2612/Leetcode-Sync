class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        d = Counter(nums)
        s = set()

        def backtracking(i, cur):
            if i == len(nums):
                temp = ''.join(str(j) for j in cur)
                if temp not in s:
                    ans.append(cur[:])
                    s.add(temp)
                return
            
            for c in nums:
                if d[c] > 0:
                    cur.append(c)
                    d[c] -= 1
                    backtracking(i+1, cur)
                    cur.pop()
                    d[c] += 1
        
        backtracking(0, [])
        return ans