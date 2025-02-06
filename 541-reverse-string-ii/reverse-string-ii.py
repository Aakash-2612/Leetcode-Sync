class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count = 1
        myS = ''
        for i in range(0, len(s), k):
            if count % 2 != 0:
                res = s[i:i + k]
                myS += res[::-1]
            else:
                myS += s[i:i + k]
            count += 1

        return myS