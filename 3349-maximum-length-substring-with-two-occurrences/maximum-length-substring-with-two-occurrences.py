class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        arr = [0 for i in range(26)]
        for r in range(len(s)):
            arr[ord(s[r]) - ord("a")] += 1
            while max(arr) > 2:
                arr[ord(s[l]) - ord("a")] -= 1
                l += 1
            ans = max(ans, (r - l + 1))
        return ans