class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans1 = self.helper(1, words, groups)
        ans2 = self.helper(0, words, groups)

        if len(ans1) > len(ans2):
            return ans1
        else:
            return ans2

    def helper(self, temp, words, groups):
        arr = []
        flag = True
        for index, i in enumerate(groups):
            if i == temp and flag:
                flag = False
                arr.append(words[index])
            elif i != temp and not flag:
                flag = True
                arr.append(words[index])

        return arr