class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = []
        r = []
        s = 0
        for i in nums:
            s += i
            l.append(s)
        s = 0
        for i in nums[::-1]:
            s += i
            r.append(s)
        r = r[::-1]
        # print(l)
        # print(r)
        ans = []
        for i, j in zip(l, r):
            ans.append(abs(i - j))
        return ans