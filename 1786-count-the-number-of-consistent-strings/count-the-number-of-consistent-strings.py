class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        index = 0
        count = 0
        while index != len(words):
            if all(i in allowed for i in words[index]):
                count += 1
            index += 1

        return count