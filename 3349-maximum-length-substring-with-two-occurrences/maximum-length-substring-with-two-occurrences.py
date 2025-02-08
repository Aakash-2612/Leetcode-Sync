class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            arr = [0 for i in range(26)]
            for j in range(i, len(s)):
                arr[ord(s[j]) - ord("a")] += 1
                if max(arr) > 2:
                    ans = max(ans, (j - i))
                    print(j, i)
                    break
                ans = max(ans, (j - i + 1))
        return ans