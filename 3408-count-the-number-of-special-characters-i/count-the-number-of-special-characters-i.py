class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        s = set(word)
        for i in s:
            if chr(ord(i) - 32) in s:
                count += 1

        return count