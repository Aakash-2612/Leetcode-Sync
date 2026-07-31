class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counts = [0] * 26
        for char in word:
            letter_counts[ord(char) - ord('a')] += 1
        sorted_counts = sorted(letter_counts, reverse=True)
        
        total_key_presses = 0
        for index, count in enumerate(sorted_counts):
            if count == 0:
                break
            total_key_presses += (index // 8 + 1) * count
        
        return total_key_presses