class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for i in queries:
            ind = 0
            flag = True
            for c in i:
                if ind >= len(pattern):
                    if c.isupper():
                        flag = False
                    continue
                if c.isupper():
                    if c == pattern[ind]:
                        ind += 1
                    else:
                        flag = False
                else:
                    if c == pattern[ind]:
                        ind += 1
            if ind < len(pattern):
                flag = False
            ans.append(flag)
        return ans