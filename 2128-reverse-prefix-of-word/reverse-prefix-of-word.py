class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = word
        for index, i in enumerate(word):
            if i == ch:
                ans = word[:index+1][::-1] + word[index+1:]
                break
        return ans