class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        d = Counter(digits)
        ans = []

        def backtrack(i, cur):
            if i == 3:
                if int(cur)%2 == 0 and len(str(int(cur))) == 3:
                    ans.append(cur)
                return
            for c in d:
                if d[c]:
                    d[c] -= 1
                    backtrack(i+1, cur+str(c))
                    d[c] += 1
        backtrack(0, '')
        # print(ans)
        return len(ans)
