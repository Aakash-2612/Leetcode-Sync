class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)
        a = int(s) + 1
        ans = []
        for i in str(a):
            ans.append(int(i))
        return ans