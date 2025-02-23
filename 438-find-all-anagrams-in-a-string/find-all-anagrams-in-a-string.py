class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        ans = []
        p_len = len(p)
        temp, p_arr = [0]*26, [0]*26
        p_dict = {}
        for i in p:
            p_arr[ord(i) - ord('a')] = 1
            if i not in p_dict:
                p_dict[i] = 1
            else:
                p_dict[i] += 1
                
        d = {}
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            temp[ord(s[r]) - ord('a')] = 1
            if (r - l + 1) == p_len:
                if p_arr == temp and d == p_dict:
                    ans.append(l)
                
                d[s[l]] -= 1
                if d[s[l]] > 0:
                    temp[ord(s[l]) - ord('a')] = 1
                else:
                    temp[ord(s[l]) - ord('a')] = 0
                    del d[s[l]]
                l += 1

        return ans